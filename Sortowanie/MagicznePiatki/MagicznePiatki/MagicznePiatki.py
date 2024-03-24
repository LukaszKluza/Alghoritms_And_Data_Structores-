import math


def InsertSort(T):
    n = len(T)
    for i in range(n):
        j = i-1
        x = T[i]
        while j>=0 and T[j]>x:
            T[j+1] = T[j] 
            j-=1 
        T[j+1] = x


def MagicznePiatki(T):
    n = len(T)
    if n == 1:
        return T[0]
    n1 = math.ceil(n/5)
    k = 0 
    A = [[] for _ in range(n1) ]

    for i in range(n):
       A[k//5].append(T[i])
       k+=1

    for i in range(n1):
        InsertSort(A[i])

    M = [A[i][2] for i in range(n1-1)] 
    M.append(A[n1-1][len(A[n1-1])//2])
    return MagicznePiatki(M)

def partition(T,p,k):
    A = [T[i] for i in range(p,k+1)]
    q = MagicznePiatki(A) 
    temp = -1
    i = p-1
    for j in range(p,k+1):
        if T[j]<=q:
            if T[i] == q:
                temp = i
            i+=1 
            T[i],T[j] = T[j], T[i] 
    if temp!= -1:T[i],T[temp] = T[temp], T[i]
    return i


def QuickSelect(T,p,k,x):
    q = partition(T,p,k)
    if q == x:
        return T[x] 
    if q > x:
        return QuickSelect(T,p,q-1,x)
    return QuickSelect(T,q+1,k,x)


T = [1,5,2,13,2,13,11,12,14,5,2,3,6,12,4,1,2,8,7,2,4,5]
A = sorted(T)
n = len(T)
print(A)
for i in range(n): 
    print(i,A[i],QuickSelect(T,0,len(T)-1,i))
print(QuickSelect(T,0,len(T)-1,21))
