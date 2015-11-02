
#Nested List Exercise
def printSecondLowest(Lis):
    lowest, secondLowest = float('inf'),float('inf')
    L1 = []
    for num in Lis:
        if num[1] <= lowest:
            lowest, secondLowest = num[1], lowest
        elif num[1] < secondLowest:
            secondLowest = num[1]
    for num in Lis:
        if num[1] == secondLowest:
            L1.append(num[0])
    return L1

nestedList = []
numOfInput = int(input())
for i in range(0,numOfInput):
    personName = input()
    personMarks = float(input())
    nestedList.insert(i,[personName,personMarks])
L2 = printSecondLowest(nestedList)
L2.sort()
for name in L2:
    print(name)