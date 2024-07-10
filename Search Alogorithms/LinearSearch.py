def linearSearch(lst,data):
    for i in range(len(lst)):
        if (lst[i]==data):
            return i
    return -1


if __name__=='__main__':
    lst=[4,2,6,8,1,3]
    data=4
    resultSet=linearSearch(lst,data)
    if (resultSet==-1):
       print(f"Search element {data} not found in the list {lst}")
    else:
       print(f"Search element {data}  found in the list {lst} at the index of {resultSet}")