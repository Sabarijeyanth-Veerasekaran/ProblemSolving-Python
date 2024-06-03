# Right Rotate Problem
# Input list l=[5,3,1,6,8,9]
# Output list l=[9,5,3,1,6,8]
# Roate the elements to one step right

def rightRotate(numList):
    n=len(numList)
    lastElement=numList[n-1]
    i=n-1
    while i>0: # always i > 0, if i>=0 then -1 index(last element will be replaced)
        numList[i]=numList[i-1]
        i=i-1
    numList[0]=lastElement
    return (numList)

if __name__=='__main__':
    numList=[5,3,1,6,8,9]
    print(f"Before right rotate list is {numList}")
    rightRotateList=rightRotate(numList)
    print(f"After right rotate list is {rightRotateList}")