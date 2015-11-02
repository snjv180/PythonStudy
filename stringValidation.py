def hasAlphaNum(strList):
    for s in strList:
        if s.isalnum():
            return True
    return False
        
def hasAlpha(strList):
    for s in strList:
        if s.isalpha():
            return True
    return False
        
def hasNum(strList):
    for s in strList:
        if s.isdigit():
            return True
    return False

def hasLower(strList):
    for s in strList:
        if s.islower():
            return True
    return False

def hasUpper(strList):
    for s in strList:
        if s.isupper():
            return True
    return False
        
strList = list(input())
print(hasAlphaNum(strList))
print(hasAlpha(strList))
print(hasNum(strList))
print(hasLower(strList))
print(hasUpper(strList))