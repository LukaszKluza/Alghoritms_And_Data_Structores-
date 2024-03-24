def merge(T, p, s, k ):
    L = [T[i] for i in range(p,s+1)]
    R = [T[i] for i in range(s+1,k+1)]
    n1 = len(L)
    n2 = len(R)
    l = 0
    r = 0
    while l < n1 and r < n2:
        if L[l] <= R[r]:
            T[p] = L[l] 
            l += 1
        else:
            T[p] = R[r] 
            r += 1
        p+=1 
    while l < n1:
        T[p] = L[l] 
        l += 1 
        p += 1
    while r < n2: 
        T[p] = R[r]
        r += 1 
        p += 1


def merge_sort(T,p,k):
    if p >= k:
        return
    s = (p+k)//2
    merge_sort(T,p,s)
    merge_sort(T,s+1,k)
    merge(T,p,s,k)


#T = [6,2,3,9,6,5]
T = [1.1,1.8,3.2,6,4.2,2.9,3.7,0.3,0.9]
merge_sort(T,0,len(T)-1)

print(T)