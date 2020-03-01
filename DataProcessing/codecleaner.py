import csv as csv

# when there is a <code> opening tag, everything until the next </code> will be ignored
# also wehen a <pre> opening tag is used and the next tag is also a <code> tag then everything within the <pre> must be ignored
def cleanCodePassage(currentOuterCounter, bodyText, searchText):
    #print("cleanCodePasaage with search for " + searchText + ".")
    # +length because the substring method is [index, index2)
    while bodyText[currentOuterCounter:currentOuterCounter+len(searchText)].lower() != searchText:
        # step through the code passage
        currentOuterCounter += 1
    # now behind the code passage so return the new pointer position
    return currentOuterCounter + len(searchText) -1
def cleanCode(openFile, writeFile):
    currentCSVFile = open(openFile, mode="r", encoding="utf8")
    reader = csv.reader(currentCSVFile, delimiter=',')
    cleanedCSVFile = open(writeFile, mode="w", newline='', encoding="utf8")
    writer = csv.writer(cleanedCSVFile, delimiter=',')
    rowCC = 0
    for row in reader:
        rowCC += 1
        #print("In row " + str(rowCC))
        rowBody = row[8]
        counter = 0
        newBody = ""
    # begin of parsing until the end of file
    # print("started new row: " + row)
        while counter != len(rowBody):
            # when a tag begins
            if rowBody[counter] == "<":
                # if the found tag starts with code, then we ignore the whole innerHTML
                if rowBody[counter+1:counter+5] == "code":
                    if rowCC == 40459:
                        print("code tag")
                    counter = cleanCodePassage(counter, rowBody, "</code>")
                # if the found tag is a link tag which looks like <a link....> we also want to remove that completely because the text is most likely the link directly, so we do not want to analyze this
                elif rowBody[counter+1:counter+2] == "a" and rowBody[counter+2] == ' ':
                    if rowCC == 40459:
                        print("link tag")
                    counter = cleanCodePassage(counter, rowBody, "</a>")
                # else it is a tag which does not require it's innerHTML to be removed, so we only remove the tag itself
                else:
                    # start search for end of the tag, so that it can be removed
                    secondCounter = counter
                    if rowCC == 40459:
                        print("normal tag")
                    while rowBody[secondCounter] != ">" and secondCounter < len(rowBody):
                        secondCounter += 1
                        if rowCC == 40459:
                            print("searching tag end")
                    counter = secondCounter
                    # print(rowBody[counter])
            else:
                newBody += rowBody[counter]
            counter += 1
        row[8] = newBody
        writer.writerow(row)


if __name__ == '__main__':

    nameFile = open("./allJointFiles.txt", mode="r", encoding="utf8")
    rows = nameFile.read().splitlines()
    for r in rows:
        cleanedFileName = r[0:len(r)-4]+"_Cleaned"+".csv"
        print("Started processing file " + cleanedFileName + ".")
        cleanCode("./JointFiles/"+r, "./CleanedFiles/"+cleanedFileName)
        print("Finished processing file " + cleanedFileName + ".")