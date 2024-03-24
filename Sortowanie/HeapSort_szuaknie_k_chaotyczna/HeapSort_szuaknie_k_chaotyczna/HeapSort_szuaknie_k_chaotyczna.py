def heapify(T,x,idx,n):
    max_int = x
    l = 2*x+1
    r = 2*x+2
    if l<n and T[l][idx]>T[max_int][idx]:
        max_int = l 
    if r<n and T[r][idx]>T[max_int][idx]:
        max_int = r
    if x != max_int:
        T[x],T[max_int] = T[max_int],T[x]
        return heapify(T,max_int,idx,n)

def bulid_heap(T,idx):
    n = len(T)
    ran = (n-2)//2
    for i in range(ran,-1,-1):
        heapify(T,i,idx,n)

def HeapSort(T,idx=0):
    n = len(T)
    bulid_heap(T,idx)
    for i in range(n-1,-1,-1):
        T[i],T[0] = T[0],T[i] 
        heapify(T,0,idx,i)

T = [0,4,8,1,2,9,2,3,17,8,3]

T2 = [
    [6,9],
    [2,4],
    [3,6],
    [0,0],
    [5,8],
    [4,6],
    [1,0]
    ]

A = [0,2,1.1,2]
HeapSort(T2,1) 
print(T2)
