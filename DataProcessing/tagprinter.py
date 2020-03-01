import csv as csv

file = open("./CleanedFiles/C_Answers_2008_cleaned.csv", mode="r", encoding="utf8")
files = open("TagExampleUse.txt", mode="w",encoding="utf8")
tagfile = open("./Tags.txt", mode="r", encoding="utf8")
reader = csv.reader(file, delimiter = ",")
counter = 0
tags = ["<img>", "<a>"]
alreadyFoundTags = []
tags = tags + tagfile.read().splitlines()

for row in reader:
    body = row[8]
    print(row[0])
    #if counter > 20:
    #    break
    #counter += 1
    writeline = False
    inThisBody = []
    for x in tags:
        if x in body and x not in alreadyFoundTags:
            alreadyFoundTags.append(x)
            inThisBody.append(x)
            writeline = True
    if writeline:
        files.write(body)
        writeline = False
        files.write("Example of " +  str(inThisBody) + "in post " + str(row[0]) + "\n//////////////////////////////////////////////////////////////////////////////////////////\n")