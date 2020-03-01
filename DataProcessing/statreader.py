import csv as csv
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("./JointFiles/") if isfile(join("./JointFiles/", f))]

numberOfRowsPython = 0
numberOfRowsC = 0

for fileName in onlyfiles:
    file = open("./JointFiles/" + fileName, mode = "r", encoding="utf8")
    fReader = csv.reader(file, delimiter = ",")
    yearReader = 0
    firstRow = True
    for row in fReader:
        if firstRow:
            firstRow = False
            continue
        if 'C' in fileName:
            numberOfRowsC += 1
        else:
            numberOfRowsPython += 1
        yearReader += 1
    if 'C' in fileName:
        print("In " + fileName[10:14] + " the C community has answered " + str(yearReader) + " questions.")
    else:
        print("In " + fileName[15:19] + " the Python community has answered " + str(yearReader) + " times.")
print("The C community has answered a total of " + str(numberOfRowsC) + " times.")
print("The Python community has answered a total of " + str(numberOfRowsPython) + " times.")
print("In total the dataset contains " + str((numberOfRowsC+numberOfRowsPython))+  " answers.")