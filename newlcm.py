from math import sqrt

def getPrimes(n):
        sqrt_n = int(sqrt(n))
        no_primes = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)}
        primes = {i for i in range(n) if i not in no_primes}
        primes.remove(0)
        primes.remove(1)
        return list(primes)

def canDivide(list,primeNum):
        divideCounter = 0
        for i in list:
                if (i%primeNum == 0):
                        divideCounter += 1
        if divideCounter >= 2:
                return True
        else:
                return False

def getDividedList(list,primeNum):
        result = []
        for i in list:
                if(i%primeNum ==0):
                        result.append(i//primeNum)
                else:
                        result.append(i)
        return result

def getMultipliedResult(mergedList):
        result = 1
        for i in mergedList:
                result *= i
        return result

def smallest(n):
        lis = list(range(1,n+1))
        needToDivide = False
        primes = getPrimes(n)
        primeList = []
        quotientList = []
        while primes:
                if canDivide(lis,primes[0]):
                        quotientList.append(primes[0])
                        lis = getDividedList(lis,primes[0])
                else:
                        primes.pop(0)
        mergedList = quotientList + lis
        result = getMultipliedResult(mergedList)
        return result

print(smallest(10))
