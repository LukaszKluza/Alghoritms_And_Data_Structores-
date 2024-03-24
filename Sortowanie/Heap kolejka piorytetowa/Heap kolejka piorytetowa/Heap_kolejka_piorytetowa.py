def Heapify(T,i,n):
    max_int = i
    l = i*2+1
    r = i*2+2
    if l<n and T[l] > T[max_int]:
        max_int = l 
    if r<n and T[r] > T[max_int]:
        max_int = r 
    if max_int != i:
        T[max_int],T[i] = T[i],T[max_int] 
        Heapify(T,max_int,n)

def BuildHeap(T):
    n = len(T) 
    p = (n-2)//2
    for i in range(p,-1,-1):
        Heapify(i) 

def insert(T,x):
    n = len(T)
    p = (n-1)//2
    T.append(x)
    while p>=0:
        print(T[p],T[n])
        if T[p] <  T[n]:
            T[p],T[n] = T[n],T[p] 
        else:
            return 
        n = p 
        p = (p-1)//2
    return


def pop_q(T): 
    if len(T) == 0:
        return None
    return T.pop(0)


T = [] 
insert(T,1)
print(T)
insert(T,4)
print(T)
insert(T,9)
print(T)
print(pop_q(T))
print(T)
print(pop_q(T))
print(T)
print(pop_q(T))
print(T)
print(pop_q(T))
print(T)