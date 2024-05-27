#Two Sum Problem
#input l=[4,7,2,11,9]
#output o=13 --> 2+11 result index will be 2 and 3
#Approach
# Calculating differnece between the targer and values present in list and checking if current values already present in the dict
#If present then returing current index and index of diff value
#If not presnr then adding the diff to dictionary in the format of key - diff and value - i


def twoSum(numList,target):
    diff=0
    diffList={}
    for i in range (len(numList)):
        diff=target-numList[i]
        if numList[i] in diffList:
            return (numList.index(diff),i, diff+numList[i])
        diffList[diff]=i



if __name__=='__main__':
    nums=[4,7,2,11,9]
    target=123
    result=twoSum(nums,target)
    if result is  None:
        print(f"There are no integers present in list which can be added to get {target}")
    else:
        print(f"Index of the integer which can added to get {result[2]} are {result[0]},{result[1]}.")

