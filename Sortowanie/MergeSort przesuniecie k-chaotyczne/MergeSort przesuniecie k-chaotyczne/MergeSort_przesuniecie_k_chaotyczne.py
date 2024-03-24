def Merge(T,p,s,k,idx):
    L = [T[i] for i in range(p,s+1)]
    R = [T[i] for i in range(s+1,k+1)]
    nl = len(L)
    nr = len(R)
    l = r = 0
    while l<nl and r < nr:
        if L[l][idx] <= R[r][idx]:
            T[p] = L[l] 
            l += 1
        else:
            T[p] = R[r] 
            r += 1
        p += 1

    while l <nl:
        T[p] = L[l] 
        l += 1
        p += 1

    while r<nr:
        T[p] = R[r] 
        r += 1 
        p += 1

def MergeSort(T,p,k,idx):
    if p >= k:
        return
    s = (p+k)//2
    MergeSort(T,p,s,idx)
    MergeSort(T,s+1,k,idx)
    Merge(T,p,s,k,idx)


def solve(T):
    n = len(T)
    A = [[] for i in range(n)]
    for i in range(n):
        A[i].append(T[i])
        A[i].append(i)
    MergeSort(A,0,n-1,0)
    res = 0
    for i in range(n):
        res = max(res,abs(i-A[i][1]))
    print(A)
    print(res)
#T = [[0,0],[2,1],[1.1,2],[2,3]]
T = [0,2,1.1,2]

solve(T)
#MergeSort(T,0,len(T)-1,0) 

