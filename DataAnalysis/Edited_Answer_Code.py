import csv




def calculate_average_of_words_in_answers():
    file = open("./QueryDumps/c_unedited_Questions.csv", mode="r", encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    i = 0
    sum_of_Words = 0.0
    sum_of_scores = 0.0
    sum_of_comments = 0.0
    for row in reader:
        i += 1
        words = row[0].split()
        sum_of_comments += float(row[1])
        sum_of_scores += float(row[2])
        sum_of_Words += len(words)
    print("The Texts have an average of ", (sum_of_Words/i), "words, the average score is", (sum_of_scores/i), "and the average comment count is", (sum_of_comments/i))

#calculate_average_of_words_in_answers()

def calculate_statistics_of_top_answers():
    file = open("./QueryDumps/Most_Negative_answers_C_Compound_All.csv", mode="r", encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    i = 0
    commentscore = 0
    votescore = 0
    for row in reader:
        commentscore += float(row[1])
        votescore += float(row[8])
        i += 1
    print("The most negative answers of C have a commentcount on average of ", (commentscore/i), "and a voting score of ", (votescore/i))

calculate_statistics_of_top_answers()
