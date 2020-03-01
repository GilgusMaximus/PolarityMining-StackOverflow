import csv as csv

filenames = ["Python_Answers_2019_Jan.csv", "Python_Answers_2019_Feb.csv", "Python_Answers_2019_Mar.csv", "Python_Answers_2019_Apr.csv", 
"Python_Answers_2019_May.csv", "Python_Answers_2019_June.csv", "Python_Answers_2019_July.csv", "Python_Answers_2019_Aug.csv", "Python_Answers_2019_Sep.csv", 
"Python_Answers_2019_Oct.csv", "Python_Answers_2019_Nov.csv", "Python_Answers_2019_Dec_2.csv"]

joinedCSVFile = open("./JointFiles/Python_Answers_2019.csv", mode="w", newline='', encoding="utf8")


csvWriter = csv.writer(joinedCSVFile, delimiter=',')
firstFile = True
rowCounterOfSingleFiles = 0
rowCounterOfWholeFile = 0
for filename in filenames:
    counter = 0
    currentCSVFile = open("E:/Downloads/Queries/"+filename, mode = "r", encoding="utf8")
    csvReader = csv.reader(currentCSVFile, delimiter=',')
    for row in csvReader:
        rowCounterOfSingleFiles += 1
        #if we are in row 1 or higher, we take all rows, but if we are in row 0, we only want to take the one of the first file, otherwise we copy the header line multiple times
        if counter >= 1 or (firstFile and counter == 0) :
            csvWriter.writerow(row)
            rowCounterOfWholeFile += 1
            firstFile = False
            counter += 1
        # print(row)
        counter += 1
print("The " + str(len(filenames)) + " single files had a total of " + str(rowCounterOfSingleFiles) + " rows.")
print("The whole file has a total of " + str(rowCounterOfWholeFile) + " rows. Because the first row of every file other than the first is left out to prevent having the header line copied multiple times, the number of rows it should have: " + str((rowCounterOfSingleFiles-len(filenames)+1)))
