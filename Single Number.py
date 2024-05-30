# Single Number Problem
# Input : [5,3,4,3,4]
# Output : 5
# In the given list, have to find which number appeared only once
# Approach
# Do XOR operation on the list elements in the array

def singleNumber(numList):
    singleNum=0
    for num in numList :
        singleNum=singleNum^num
    return singleNum

if __name__ == '__main__' :
    numList=[5,3,4,3,4]
    singleNum=singleNumber(numList)
    print(f"The single number present in {numList} is {singleNum}")