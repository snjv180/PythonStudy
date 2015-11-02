#Task 
#You are given an integer N in one line. The next line contains N space-separated integers. Create a tuple of those N integers. Lets call it T. 
#Compute hash(T) and print it.
#
#Note hash() is one of the function in __builtins__ module.
#
#Input Format 
#The first line contains N. The next line contains N space-separated integer values.
#
#Output Format 
#Print the computed value.
#
#Sample Input
#
#2
#1 2
#Sample Output
#
#3713081631934410656

numOfInput=int(input())
l = []
inputVals = input().split()
for i in range(0,numOfInput):
    l.insert(i,int(inputVals[i]))
mytuple = tuple(l)
print(hash(mytuple))