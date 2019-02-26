#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures
test = "abcdef"
charSet = 128 * [False]

def IsUnique(stringToTest):
    if(len(stringToTest)>128):
        return false
    for c in stringToTest:
        charValue = ord(c)
        if(charSet[charValue]):
            return False
        else:
            charSet[charValue] = True
    
    return True   

answer = IsUnique(test)
print(answer)
