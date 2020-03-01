import csv as csv

file = open("./JointFiles/C_Answers_2018.csv", mode="r", encoding="utf8")
files = open("./Tags.txt", mode="w",encoding="utf8")
reader = csv.reader(file, delimiter = ",")
seenTags = ["<a>", "<img>"]
for row in reader:
    #if counter > 20:
    #    break

    body = row[8]
    for counter in range(len(body)):
        if body[counter] == '<':
            innerCounter = counter
            while body[innerCounter] != '>':
                innerCounter += 1
            tag = body[counter:innerCounter+1]
            if tag not in seenTags and tag[1] != 'a' and tag[1:4] != "img":
                seenTags.append(tag)
                files.write(tag + "\n")


   # files.write(row[8])
   # files.write("//////////////////////////////////////////////////////////////////////////////////////////\n")