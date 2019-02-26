# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
string1 = "quick brown fox"
string2 = "jumped over a lazy dog"
charCount = 128 * [0]

def checkPermutation(string1, string2):
    if(len(string1) != len(string2)):
        return False
    
    for c in string1:
        charValue = ord(c)
        charCount[charValue] += 1
    
    for c in string2:
        charValue = ord(c)
        charCount[charValue] -= 1
        if(charCount[charValue]<0):
            return False
    return True

answer = checkPermutation(string1, string2)
print(answer)
    
