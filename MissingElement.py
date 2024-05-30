#Missing Element Problem
# To Find missing element from 1 to n list
#Input [1,2,3,5,6]
#Output 4 --> Since 4 is missing in the list
#Approach
#Step 1: Calculting sum value of 1,2,3,4,5,6
#By using sum formula = n*(n+1)/2
#Step 2: Then calculating sum of elements present in list
#Subracting Step 1 and Step 2 sum then we will get missing element value.

def missingElement(numList,n):
    sumValue=n*(n+1)/2
    # List sum value
    listSum=sum(numList)
    missingValue=sumValue-listSum
    return missingValue

if __name__=='__main__' :
    n=6
    list=[1,2,3,5,6]
    missingValue=missingElement(list,n)
    print(f"Missing value in list from 1 to {n} is {missingValue}")

