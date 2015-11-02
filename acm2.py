from math import sqrt

def getPrimes(n):
        sqrt_n = int(sqrt(n))
        no_primes = [j for i in range(2,sqrt_n) for j in range(i*2, n, i)]
        primes = set([i for i in range(n) if i not in no_primes])
        primes.remove(0)
        primes.remove(1)
        return primes

def getList(m):
    lis = list(map(int,str(m)))
    return [i ** 2 for i in lis]
    
def reduceNum(m):
    if m == 1:
        return 1
    else:
        return reduceNum(sum(getList(m)))
        

def checkNum(k,m):
    primes = getPrimes(m+1)
    if m not in primes:
        print("%d %d %s"%(k,m,"NO"))
    else:
        if reduceNum(m) == 1:
            print("%d %d %s"%(k,m, "YES"))
        else:
            print("%d %d %s"%(k,m, "NO"))
    

P = int(input())
if P >= 1 and P <= 1000:
    for i in range(0, P):
        val = input().split()
        k , m = int(val[0]),int(val[1])
        if m == 1  or m > 10000:
            print("%d %d %s"%(k,m,"NO"))
            continue
        else:
            checkNum(k,m)
