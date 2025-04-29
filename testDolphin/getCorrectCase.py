import os
import re

sourceBasePath = "/home/luwei/code/sqllogictest/tempRes/random/aggregates"
verifyResBasePath = "/home/luwei/code/sqllogictest/verifyRes/random/aggregates"
outBasePath = "/home/luwei/code/sqllogictest/correctCase/random/aggregates"


sourceFiles = [f for f in os.listdir(sourceBasePath) if os.path.isfile(os.path.join(sourceBasePath, f))]
# sourceFiles = [
#     "select1.test"
# ]

if not os.path.exists(outBasePath):
    os.makedirs(outBasePath)

def getNextRecord(i, lines, length):
    if i == 0:
        return 0
    else:
        while i < length and len(lines[i].strip()) != 0:
            i += 1
        
        return i+1 

for sFile in sourceFiles:
    sourceFilePath = os.path.join(sourceBasePath, sFile)
    verifyResFilePath = os.path.join(verifyResBasePath, sFile)
    outFilePath = os.path.join(outBasePath, sFile)

    with open(verifyResFilePath, "r") as fin:
        text = fin.read()

        indexes = re.findall(r'.test:(\d+):', text)
        indexes = [int(i) for i in indexes]
        indexes = sorted(indexes)
        print(indexes)

        newLines = []
        with open(sourceFilePath, "r") as sfin:
            lines = sfin.readlines()
            length = len(lines)
            l = 0
            nextInd = getNextRecord(1, lines, length)
            p = 0
            while l < length:
                if p < len(indexes) and indexes[p] > l and nextInd > indexes[p]:
                    while p < len(indexes) and indexes[p] < nextInd:
                        p += 1
                    l = nextInd
                    nextInd = getNextRecord(nextInd, lines, length)
                else:
                    if lines[l].find("onlyif") != -1:
                        l = nextInd
                        nextInd = getNextRecord(nextInd, lines, length)
                        continue

                    tmpStr = "".join(lines[l:nextInd])
                    if tmpStr.find("query") != -1 and tmpStr.find("----") == -1:
                        l = nextInd
                        nextInd = getNextRecord(nextInd, lines, length)
                        continue
                    
                    while l < nextInd:
                        newLines.append(lines[l][:])
                        l += 1
                    nextInd = getNextRecord(nextInd, lines, length)
                
        newText = "".join(newLines)
        # print(newText)
        with open(outFilePath, "w") as fout:
            fout.write(newText)

