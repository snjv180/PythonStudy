def getDivN(N):
    for i in range(1, N):
        for j in range(1,N):
            res = 3 * j + 5 * i
            if (res == N):
                return "5"*3*j+"3"*5*i
    return "-1"

def returnLargestDecNum(N):
    result = "-1"
    if N % 3 == 0:
        result = "5"*N
    elif getDivN(N) != "-1":
        result = getDivN(N)
    elif N % 5 == 0:
        result = "3"*N
    else:
        result = -1
    return result
        
T = int(input())
if T >= 1 and T <=20:
    for i in range(0, T):
        N = int(input())
        if N >= 1 and N <= 100000:
            print(returnLargestDecNum(N))
