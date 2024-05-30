# Second Largest Value Problem
# Input : [1,2,5,3,2,5,9,3,2,8,9,3]
# Output : 8

def findSecondLargest(numList):
    firstLargest=numList[0]
    print(firstLargest)
    secondLargest=0
    for i in range(1,len(numList)):
        if numList[i]>firstLargest:
            secondLargest=firstLargest
            firstLargest=numList[i]
        elif numList[i]>secondLargest and numList[i]!=firstLargest:
            secondLargest=numList[i]
    return secondLargest

if __name__=='__main__':
    numList=[1,2,5,3,2,5,9,3,2,8,9,3]
    secondLargestValue=findSecondLargest(numList)
    print(f"The second largest value in {numList} is {secondLargestValue}")