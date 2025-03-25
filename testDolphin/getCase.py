import os

scriptPath = "/home/luwei/code/sqllogictest/testDolphin/random/aggregates/slt_good_0.test"

def getNextRecord(i, lines, length):
    if i == 0:
        return 0
    else:
        while i < length and len(lines[i].strip()) != 0:
            i += 1
        
        return i+1 

def getCase(lines, length, startIndex):
    newLines = []

    i = 0
    nextInd = getNextRecord(i+1, lines, length)
    while i < startIndex:
        while i < nextInd and (lines[i].find("statement") == -1 and lines[i].find("query") == -1):
            i += 1
        if lines[i].find("statement") != -1:
            i += 1
            while i < nextInd:
                newLines.append(lines[i][:])
                i += 1

        i = nextInd
        nextInd = getNextRecord(i, lines, length)
    
    i = startIndex
    newText = getNextRecord(i, lines, length)
    while i < nextInd:
        while i < nextInd and (lines[i].find("statement") == -1 and lines[i].find("query") == -1):
            i += 1
        if lines[i].find("query") != -1:
            i += 1
            while i < nextInd:
                newLines.append(lines[i][:])
                i += 1

    newText = "".join(newLines)

    return newText


if __name__ == "__main__":

    with open(scriptPath, "r") as fin:
        lines = fin.readlines()
        length = len(lines)

        text = getCase(lines, length, 5786)

        with open("/home/luwei/code/sqllogictest/testDolphin/case.dos", "w") as fout:
            fout.write(text)

