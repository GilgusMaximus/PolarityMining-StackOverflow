import psycopg2 as postgres
import csv as csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentimentAnalyzer = SentimentIntensityAnalyzer()
# create connection to the database
databaseConnection = postgres.connect(host="localhost", dbname="DataAnalytics", user="postgres", password="1")
# create a cursor to execute commands
databaseCursor = databaseConnection.cursor()

nameFile = open("./allCleanedFiles.txt", "r", encoding="utf8")
lines = nameFile.read().splitlines()

def sentiment_analyzer_scores(sentence):
    score = sentimentAnalyzer.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))
    #print(type(score))
    return score

# build a correctly formatted string
def build_tuple_string(arrayOfStrings):
    insertString = "'" + str(arrayOfStrings[0]) +"'"
    for i in range(1, len(arrayOfStrings)):
        string = str(arrayOfStrings[i])
        #this is done to prevent an sql error because one value is no available for some reason
        if string == '':
            string = str(-1)
        insertString += ", '" + string  + "' "
    return insertString


def insert_tuple_into_database(tuple):
    databaseCursor.execute(
        """INSERT INTO Posts (Id, ParentId, CreationDate, Score, Body, OwnerUserId, LastEditorUserID, LastEditDate, CommentCount, positiveavg, negativeavg, neutralavg, compundavg, positiveall, negativeall, neutralall, compoundall, community) VALUES ({})""".format(tuple))

#if no editor is in the tuple, we simply omit the insert of the editor and date
def insert_tuple_into_database_without_editor(tuple):
    databaseCursor.execute(
        """INSERT INTO Posts (Id, ParentId, CreationDate, Score, Body, OwnerUserId, CommentCount, positiveavg, negativeavg, neutralavg, compundavg, positiveall, negativeall, neutralall, compoundall, community) VALUES ({})""".format(tuple))





for lineFile in lines:
    print("Opening file: " + lineFile)
    file = open("./CleanedFiles/"+lineFile, encoding="utf8", mode="r")
    reader = csv.reader(file, delimiter=',')
    communityValue = -1
    if lineFile[0] == "C":
        #c answer
        communityValue = 0
    else:
        # python answers
        communityValue = 1

    insertionCounter = 0
    ignoredCounter = 0


    # analyze the score

    # after a certain amount of rows the data should be committed into the database so that it doesn't have to commit all
    # tuples at the end
    rowCounter = 0
    for row in reader:
        if rowCounter == 0:
            rowCounter += 1
            continue
        rowCounter += 1
        body = row[8]
        # needed because the sql command cannot handle strings with ' as it is the sql string symbol
        body = body.replace("'", " ")
        #some answers were just code, so these were completely wiped out and now do not have anything to analyze
        if len(body) == 0:
            ignoredCounter += 1
            continue
        # get the single liens of the string
        linesOfBody = body.splitlines()

        # I average the value of the sum of values of  all lines and also further down analyze the whole body at once to have a comparison for the analysis
        sumOfScores = [0, 0, 0, 0]
        emptyLinesCounter = 0
        #print(rowCounter-1)
        for line in linesOfBody:
            if line != "":
                score = sentiment_analyzer_scores(line)
                sumOfScores[0] += score["neg"]
                sumOfScores[1] += score["neu"]
                sumOfScores[2] += score["pos"]
                sumOfScores[3] += score["compound"]
            else:
                emptyLinesCounter += 1
        wholeScore = sentiment_analyzer_scores(body)

        # some posts still have newline characters, so they are not caught by the previous empty check
        if len(linesOfBody) - emptyLinesCounter == 0:
            ignoredCounter += 1
            continue
        #average all the values
        sumOfScores[0] = sumOfScores[0]/(len(linesOfBody)-emptyLinesCounter)
        sumOfScores[1] = sumOfScores[1] / (len(linesOfBody) - emptyLinesCounter)
        sumOfScores[2] = sumOfScores[2] / (len(linesOfBody) - emptyLinesCounter)
        sumOfScores[3] = sumOfScores[3] / (len(linesOfBody) - emptyLinesCounter)

        lasteditdate = row[13]
        lasteditorid = row[11]
        tupleString = ""
        if lasteditdate == '' or lasteditorid == '':
            tupleString = build_tuple_string(
                [row[0], row[3], row[4], row[6], body, row[9], row[18], sumOfScores[2],
                sumOfScores[0], sumOfScores[1], sumOfScores[3], wholeScore["pos"], wholeScore["neg"], wholeScore["neu"],
                wholeScore["compound"], communityValue])
            insert_tuple_into_database_without_editor(tupleString)
            insertionCounter += 1
        else:
            tupleString = build_tuple_string([row[0], row[3], row[4], row[6], body, row[9], lasteditorid, lasteditdate, row[18], sumOfScores[2], sumOfScores[0], sumOfScores[1], sumOfScores[3], wholeScore["pos"], wholeScore["neg"], wholeScore["neu"], wholeScore["compound"], communityValue])

            insert_tuple_into_database(tupleString)

            insertionCounter += 1
    # exit(0)

    # commit all tuples into the databse
    databaseConnection.commit()
    print("Inserted " + str(insertionCounter) + " into " + lineFile + " tuples and omitted " + str(ignoredCounter) + " tuples because of no text in the answer body after code cleaning.")
    print("There were " + str(rowCounter) + " tuples in total and " + str(rowCounter-ignoredCounter-1) + " should have been inserted from that. Do the values match?")
    # example tupel
    # testTupel = "'555555', '5555', '2020-03-01 04:05:06', '2000', 'hallöle', '-5', '-100', '2020-2-12 07:08:09', '100', '0.2565', '0.356', '0.4565', '0.5565', '0.2565', '0.356', '0.4565', '0.5565'"

    # insert the current tupel

# close the cursor
databaseCursor.close()
databaseConnection.close()
