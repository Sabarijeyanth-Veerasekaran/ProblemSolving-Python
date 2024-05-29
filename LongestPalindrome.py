#Longest Palindromic Substring
#Input  : racecar
#Output : racecar , length is 7
#Input : bccd
#Output : cc , length is 2

#Approach
# Checking the left and right side character of each charatcer present in the string literal
#For odd length strings, start checking with same index character
#For even length strings, start checking with current index and index+1  character

def longestPalindrome(s: str) -> str:
  resultStr=""
  resultLen=0
  n=len(s)
  for i in range(n):
      # Extracting valid palindrome from odd length string
      leftPointer=i
      rightPointer=i
      while (leftPointer >= 0 and rightPointer < n and s[leftPointer] == s[rightPointer]):
          if (rightPointer - leftPointer + 1) > resultLen:
              resultStr = s[leftPointer:rightPointer + 1]
              resultLen=rightPointer-leftPointer+1
          leftPointer -= 1
          rightPointer += 1


      # Extracting valid palindrome from even length string
      leftPointer=i
      rightPointer=i+1
      while (leftPointer >= 0 and rightPointer < n and s[leftPointer] == s[rightPointer]):
          if (rightPointer - leftPointer + 1) > resultLen:
              resultStr = s[leftPointer:rightPointer + 1]
              resultLen = rightPointer - leftPointer + 1
          leftPointer -= 1
          rightPointer += 1


  return(resultStr,resultLen)


if __name__=='__main__':
    resultSet=longestPalindrome("racecar")
    print(f"Longest Substring Palindrome is {resultSet[0]} and length is {resultSet[1]}")