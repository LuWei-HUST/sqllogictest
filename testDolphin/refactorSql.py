import os
import re

basepath = "/home/luwei/code/sqllogictest/test/random/aggregates"
outbasepath = "/home/luwei/code/sqllogictest/testDolphin/random/aggregates"
resbasepath = "/home/luwei/code/sqllogictest/tempRes/random/aggregates"
verifyResBasePath = "/home/luwei/code/sqllogictest/verifyRes/random/aggregates"

sourceFiles = [f for f in os.listdir(basepath) if os.path.isfile(os.path.join(basepath, f))]
# sourceFiles = [
#     "slt_good_0.test"
# ]

if not os.path.exists(outbasepath):
    os.makedirs(outbasepath)

if not os.path.exists(resbasepath):
    os.makedirs(resbasepath)

if not os.path.exists(verifyResBasePath):
    os.makedirs(verifyResBasePath)

# print(sourceFiles)
# exit(0)

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
    # print(filepath)
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
                if lines[ind].startswith("query"):
                    newLines.append(lines[ind][:])
                    ind += 1
                else:
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
    newText = newText.replace("COUNT", "count")
    newText = newText.replace("MIN", "min")
    newText = newText.replace("MAX", "max")
    newText = newText.replace("AVG", "avg")
    newText = newText.replace("DISTINCT", "distinct")

    newText = re.sub(r'VARCHAR\(\d+\)', r'STRING', newText)

    outfilepath = os.path.join(outbasepath, sfile)
    with open(outfilepath, "w") as fout:
        fout.write(newText)

    resfilepath = os.path.join(resbasepath, sfile)
    cmdstr = "~/code/sqllogictest/src/sqllogictest --engine ODBC3 --connection 'DSN=dolphindb;DRIVER={{DolphinDB}};SERVER=127.0.0.1;PORT=8848;UID=admin;PWD=123456;' {} > {}".format(outfilepath, resfilepath)

    os.system(cmdstr)

    verifyResFilePath = os.path.join(verifyResBasePath, sfile)
    # print(verifyResFilePath)

    cmdStr = "~/code/sqllogictest/src/sqllogictest -verify {} > {}".format(resfilepath, verifyResFilePath)
    # print(cmdStr)

    os.system(cmdStr)