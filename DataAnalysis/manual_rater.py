import csv
from random import randint
from random import seed
from datetime import datetime


all_filenames = ["absolute_neutral_answers.csv", "neutral_answers.csv", "positive_answers.csv", "very_positive_answers.csv"]

seed(datetime.now())

while len(all_filenames) != 0:
    file_index = randint(0, len(all_filenames)-1)
    current_file = all_filenames.pop(file_index)
    currentCSVFile = open("./check_answers/"+current_file, mode="r", encoding="utf8")
    check_file = open("./manual_rated_check_answer/"+current_file, mode="w", newline='', encoding="utf8")

    csvWriter = csv.writer(check_file, delimiter=',')
    csvReader = csv.reader(currentCSVFile, delimiter=',')
    for row in csvReader:
        print("-------------------------------------------------------------------")
        print(row[0])
        print("--------------------------------------------------------------------")
        myCompound = float(input())
        row.append(myCompound)
        csvWriter.writerow(row)
        print(myCompound)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
