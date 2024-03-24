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
        elif L[l][0] > R[r][0]:
            T[p] = R[r] 
            r += 1 
        else: 
            if L[l][1] < R[r][0]: 
                T[p] = L[l] 
                l += 1 
            else: 
                T[p] = R[r]
                r += 1
        p += 1

    while l < n1:
        T[p] = L[l] 
        l += 1 
        p += 1
    while r < n2: 
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


T = [[1,0],[3,5],[3,4],[9,1],[3,1],[0,1],[3,4],[3,2],[4,2],[3,2]]
print(T) 
MergeSort(T,0,len(T)-1)
print(T)