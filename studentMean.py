#Code for calculating average percentage of marks obtained

def calcAvg(listVal):
    return float(sum(listVal))/len(listVal)

numOfStudents = int(input())
studentDict = {} 
for i in range(0, numOfStudents):
    varInput = input().split()
    studentName = varInput[0]
    firstMark = float(varInput[1])
    secondMark = float(varInput[2])
    thirdMark = float(varInput[3])
    studentDict[studentName] = [firstMark,secondMark,thirdMark]

searchName = input()
print( "%2.2f" % (calcAvg(studentDict[searchName])) ) 
