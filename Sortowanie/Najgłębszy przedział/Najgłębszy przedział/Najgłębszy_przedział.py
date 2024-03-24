from collections import deque

Q = deque()

def Merge(T,p,s,k):
    L = [T[i] for i in range(p,s+1)]
    R = [T[i] for i in range(s+1,k+1)]
    n1 = len(L) 
    n2 = len(R)
    l = r = 0
    while l < n1 and r < n2:
        if L[l][0] < R[r][0]:
            T[p] = L[l] 
            l += 1
        elif R[r][0] < L[l][0]: 
            T[p] = R[r] 
            r+=1
        else:
            if L[l][1] < R[r][1]:
                T[p] = L[l] 
                l+= 1
            else: 
                T[p] = R[r] 
                r+=1
        p += 1
    while l<n1:
        T[p] = L[l] 
        l += 1
        p += 1
    while r<n2:
        T[p] = R[r] 
        r += 1
        p += 1

def MergeSort(T,p,k):
    if p>=k:
        return 
    s = (p+k)//2
    MergeSort(T,p,s)
    MergeSort(T,s+1,k)
    Merge(T,p,s,k)

def depth(L):
    n = len(L) 
    x = L[0]
    res = 0
    for i in range(1,n):
        print(L[i][0])
        print(x[0])
        if L[i][0] >= x[0] and L[i][1] < x[1]:
            Q.append(L[i]) 
        elif L[i][0] > x[1]:
            Q.clear()
        else:
            res = max(res, len(Q))
            x = L[i]
            while Q[0][0] < x[0] or 





#Zjebane zadanie

T = [[1,6],[5,6],[2,5],[8,9],[1,6]]
MergeSort(T,0,len(T)-1)
depth(T)