def listTest(aList):
    aList[2] = 10
    for i in range(len(theList)):
        print(aList[i])
if __name__=="__main__":
    theList = [2,8,34]
    listTest(theList)
    for i in range(len(theList)):
        print(theList[i])
