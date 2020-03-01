import csv

all_filenames = [ "very_negative_answers.csv", "negative_answers.csv", "absolute_neutral_answers.csv", "neutral_answers.csv", "positive_answers.csv", "very_positive_answers.csv"]




results = []

for current_file in all_filenames:
    currentCSVFile = open("./differences_compound/"+current_file, mode="r", encoding="utf8")

    csvReader = csv.reader(currentCSVFile, delimiter=',')

    average_my_voting = 0
    average_original = 0
    index = 0
    same_labelling_count = 0
    others_voted_id = []
    for row in csvReader:
        my_score = float(row[3])
        score = float(row[4])
        average_my_voting += my_score
        average_original += score
        index += 1
        if abs(my_score - score) < 0.1:
            same_labelling_count += 1
            others_voted_id.append(row[2])
    results.append([(average_my_voting/index), (average_original/index), same_labelling_count, others_voted_id, current_file])

for row in results:
    print("For file", row[4], "my average rating was", row[0], "while the average rating of VADER was", row[1], ". The two votings has larger disparities ", 20-row[2], " times.")
