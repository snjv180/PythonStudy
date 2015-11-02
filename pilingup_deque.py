#Problem Statement
#
#There is a horizontal row of n cubes. Side length of each cube from left to right is given. You need to create a new vertical pile of cubes. The new pile should be such that if cubei is on cubej then sideLengthj=sideLengthi. But at a time, you can only pick either the leftmost or the rightmost cube only. Print "Yes" if its possible, "No" otherwise.
#
#Input Format
#
#First line contains a single integer T, denoting the number of test cases. 
#For each testcase, there are 2 lines. 
#First line of each test case contains n. 
#Second line of each test case contains n space separated integers, the sideLengths of the cubes in that order.
#
#Constraints 
#1=T=5 
#1=n=105 
#1=sideLength<231
#Output Format
#
#For each testcase, output a single line containing a single word, either a "Yes" or a "No".
#
#Sample Input
#
#2
#6
#4 3 2 1 3 4
#3
#1 3 2
#Sample Output
#
#Yes
#No
#Explanation
#
#In the first sample, pick in this order: left, right, left, right, left, right. 
#In the second sample no order gives an appropriate arrangement since 3 will always come after either 1 or 2.

from collections import deque

numOfTestCases = int(input())
for i in range(0,numOfTestCases):
    numTestPoints = int(input())
    lis = deque(map(int,input().split()))
    condition = False
    verticalList = []
    for j in range(0, numTestPoints):
        if lis[0] >= lis[-1]:
            verticalList.append(lis.popleft())
        else:
            verticalList.append(lis.pop())
    for k in range(0, (numTestPoints-1)):
        if verticalList[k] >= verticalList[k+1]:
            condition = True
        else:
            condition = False
            break
    if condition:
        print("Yes")
    else:
        print("No")