
def mergeSort(A,p,r):
    if (p < r):
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(0,n1):
        L.append(A[p+i-1])
    for j in range(0,n2):
        R.append(A[q+j])
    L.append(99999)
    R.append(99999)
    i = 0
    j = 0
    for k in range(p-1,r-1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

Lis = [10,12,15,8,9,6,99,88,71,23]   
mergeSort(Lis,1,len(Lis))
print(Lis)
