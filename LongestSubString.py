# Longest Sub String Problem
#input s="sabari"
#l = ['sab','bari']
#output o="bari" --> length of substring is 4
#Approach
# Checking if the character present in set, if present then deleting all existing characters until actual character hits
# example (s,a,b) --> checking if a present in (s,a,b) set and deleting s,a -->(b) and adding a to end of set (b,a)
#Then checking maximum length of the substring by using max method on exiting max length and current substring length


def longestSubString(str):
    n=len(str)
    maxLen=0
    resultSet=set()
    substr=str[0]
    l=0
    for i in range(0,n):
        while str[i] in resultSet:
            resultSet.remove(str[l])
            l+=1
        resultSet.add(str[i])
        if(maxLen<(i-l+1)):
            substr=str[l:i+1]
        maxLen=max(maxLen,i-l+1)

    return(substr,maxLen)

if __name__=='__main__':
    result=longestSubString("Sabari")
    print(f"Longest substring is {result[0]} and length is {result[1]}")


