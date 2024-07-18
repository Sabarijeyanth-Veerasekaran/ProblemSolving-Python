#Binary Search
#Searching of element done in sorted list
#Sorted list [1,2,3,4,6,8]
# O(1) - constant time --> to find element 3
# O(log n) - worst case --> to find element 6 or 8



def binarySearch(lst,value):
    lst.sort()
    leftPointer=0
    rightPointer=len(lst)-1 # rightPointer should be len(lst)-1, the reason is we have check till the last element

    while (leftPointer<=rightPointer): # leftPointer should be less than or equal to rightPointer, because if the element present at last position then comparison will take place only if it is less than or equal to.
        midPointer = (leftPointer + rightPointer) // 2
        if (lst[midPointer]==value):
            return midPointer
        elif (value < lst[midPointer]):
            rightPointer=midPointer-1
        elif (value > lst[midPointer]):
            leftPointer = midPointer+1
    return -1

if __name__=='__main__':
    lst=[4,2,6,8,1,3]
    data=2
    resultSet=binarySearch(lst,data)
    if (resultSet==-1):
       print(f"Search element {data} not found in the list {lst}")
    else:
       print(f"Search element {data}  found in the list {lst} at the index of {resultSet}")