#Median of two sorted list
#input list1=[3,5] and list2=[1,4]
#combine these two list,after sorting find the median --> [1,3,4,5]
#output --> (3+4) / 2 --? 3.5
#Approach

def findMedianSortedList( numList1, numList2):

    numList3 = numList1 + numList2
    numList3.sort()
    n = len(numList3)
    print(f"Sorted Array after merging two list: {numList3}")
    return (((numList3[n//2-1]+numList3[n//2])/2.0) if n%2==0 else numList3[n//2])

if __name__=='__main__':
    result=findMedianSortedList([3,5],[1,4])
    print(f"Median value : {result}")




