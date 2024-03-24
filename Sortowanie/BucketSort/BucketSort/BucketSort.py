def Merge(T,p,sr,k):
    L = [T[i] for i in range(p,sr+1)]
    R = [T[i] for i in range(sr+1,k+1)]
    nl = len(L)
    nr = len(R)
    l=r=0
    while l < nl and r < nr:
        if L[l] <= R[r]:
            T[p] = L[l] 
            l += 1
        else:
            T[p] = R[r] 
            r += 1 
        p += 1
    while l < nl:
        T[p] = L[l] 
        l += 1
        p += 1

    while r < nr:
        T[p] = R[r] 
        r += 1 
        p += 1


def MergeSort(T,p,k):
    if p>=k:
        return
    sr = (p+k)//2
    MergeSort(T,p,sr)
    MergeSort(T,sr+1,k)
    Merge(T,p,sr,k)





def BucketSort(T,z):
    n = len(T)
    A = [[] for _ in range(z+1)]
    for x in T:
        A[int(x)].append(x)
    for a in A:
        MergeSort(a,0,len(a)-1)
    i =0
    for a in A:
        for l in a:
            T[i] = l
            i += 1

def solve(T,P):
    zakres = 0
    for k in P:
        zakres = max(zakres,k[1])
    BucketSort(T,zakres) 
    print(T)

T = [6.1,1.2,1.5,3.5,4.5,2.5,3.9,7.8]
P = [(1,5,0.75),(4,8,0.25)]
#MergeSort(T,0,len(T)-1)
#BucketSort(T,7)
solve(T,P)
