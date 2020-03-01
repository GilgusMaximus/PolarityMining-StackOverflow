import psycopg2 as postgres
import csv


from random import randint
from random import seed
from datetime import datetime


seed(datetime.now())
posts = []
for i in range(0, 20):
    posts.append(randint(1, 62508))


def databaseAccess(file):
    databaseConnection = postgres.connect(host="localhost", dbname="DataAnalytics", user="postgres", password="1")
# create a cursor to execute commands
    databaseCursor = databaseConnection.cursor()
    write_file = open("./differences_compound/" + file, mode="w", newline='', encoding="utf8")
    csvWriter = csv.writer(write_file, delimiter=',')

    for ids in posts:
        string = "select body, compoundall, id from posts where compoundall < -0.75 and compoundall >= -1.0 order by id offset " + str(ids) + " fetch first 1 rows only;"
        databaseCursor.execute(string)
        #databaseCursor.execute("select to_char(creationdate, 'YYYY-MM') as year_month, count(to_char(creationdate, 'YYYY-MM')) as number_of_answers from posts where community = 1 group by to_char(creationdate, 'YYYY-MM');")
        result = databaseCursor.fetchall()

        answers = []

        for row in result:
            csvWriter.writerow(row)
            print(row[0], "|", row[1], "|", row[2])


def databaseAccess2(file):
    databaseConnection = postgres.connect(host="localhost", dbname="DataAnalytics", user="postgres", password="1")
# create a cursor to execute commands
    databaseCursor = databaseConnection.cursor()
    write_file = open("./differences_compound/" + file, mode="w", newline='', encoding="utf8")
    csvWriter = csv.writer(write_file, delimiter=',')
    currentCSVFile = open("./manual_rated_check_answer/" + file, mode="r", encoding="utf8")

    csvReader = csv.reader(currentCSVFile, delimiter=',')

    for ids in csvReader:
        string = "select compundavg from posts where id = " + str(ids[2])
        databaseCursor.execute(string)
        #databaseCursor.execute("select to_char(creationdate, 'YYYY-MM') as year_month, count(to_char(creationdate, 'YYYY-MM')) as number_of_answers from posts where community = 1 group by to_char(creationdate, 'YYYY-MM');")
        result = databaseCursor.fetchall()

        answers = []

        for row in result:
            ids.append(row[0])
            csvWriter.writerow(ids)

all_filenames = [ "very_negative_answers.csv", "negative_answers.csv", "absolute_neutral_answers.csv", "neutral_answers.csv", "positive_answers.csv", "very_positive_answers.csv"]
for row in all_filenames:
    #databaseAccess(row)
    databaseAccess2(row)