import os

basepath = "/home/luwei/code/sqllogictest/test"
outbasepath = "/home/luwei/code/sqllogictest/testDolphin"
sourceFiles = [
    "select3.test",
]

def getNextRecord(i, lines, length):
    if i == 0:
        return 0
    else:
        while i < length and len(lines[i].strip()) != 0:
            i += 1
        
        return i+1  

for sfile in sourceFiles:
    newLines = []
    filepath = os.path.join(basepath, sfile)
    with open(filepath, "r") as fin:
        lines = fin.readlines()
        length = len(lines)

        ind = getNextRecord(0, lines, length)
        while ind < length:
            print("ind: ", ind)
            newLines.append(lines[ind][:])
            ind += 1
            nextInd = getNextRecord(ind, lines, length)
            while ind < length and ind < nextInd and lines[ind].strip() != "----":
                print(lines[ind])
                newLine = lines[ind].replace("e", "eCol")
                newLines.append(newLine[:])
                ind += 1
            
            # newLines.append("\n")
            if ind < length and lines[ind].strip() == "----":
                # while ind < length and ind < nextInd:
                #     newLines.append(lines[ind][:])
                #     ind += 1
                newLines.append("\n")
            else:
                # ind = nextInd
                pass
            ind = nextInd

    newText = "".join(newLines)
    newText = newText.replace("INTEGER", "INT")

    outfilepath = os.path.join(outbasepath, sfile)
    with open(outfilepath, "w") as fout:
        fout.write(newText)


