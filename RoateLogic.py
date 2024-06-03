# Left/Right Problem
# Input l [1,2,3,4,5] and pointer =3
# Output L.R : [4, 5, 6, 7, 1, 2, 3], R.R : [5, 6, 7, 1, 2, 3, 4]
# Approach
# L.R reverse(k:n),+reverse(0:k)
# R.R reverse(-k:),+reverse(:-k)

def leftRotate(numList,rotatePointer):
    n=len(numList)
    if n==0:
        return numList
    rotatePointer=rotatePointer%n
    return numList[rotatePointer:]+numList[:rotatePointer]

def rightRotate(numList,rotatePointer):
    n=len(numList)
    if n==0:
        return numList
    rotatePointer=rotatePointer%n
    return numList[-rotatePointer:]+numList[:-rotatePointer]

if __name__=='__main__':
   numList=[1, 2, 3, 4, 5, 6, 7]
   rotatePointer=3
   print(f"List Before Rotation {numList} and RotatePointer {rotatePointer}")
   print("Right Rotation:", rightRotate(numList, rotatePointer))
   print("Left Rotation:", leftRotate(numList, rotatePointer))
   numList = [1, 2, 3, 4, 5]
   rotatePointer = 6
   print(f"List Before Rotation {numList} and RotatePointer {rotatePointer}")
   print("Right Rotation:", rightRotate(numList, rotatePointer))
   print("Left Rotation:", leftRotate(numList, rotatePointer))