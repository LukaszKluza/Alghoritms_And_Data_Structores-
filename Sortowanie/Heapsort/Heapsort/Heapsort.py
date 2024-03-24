def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)//2
def heapify(T,i,n):
    max_int = i
    l = left(i)
    r = right(i)
    if l< n and T[max_int] < T[l]: max_int = l
    if r < n and T[max_int] < T[r]: max_int = r
    if i != max_int:
        T[i],T[max_int] = T[max_int],T[i]
        heapify(T,max_int,n)

def buildheap(T):
    n = len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n)

def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n-1,0,-1):
        T[i],T[0] = T[0],T[i]
        heapify(T,0,i)

T = [1,4,6,9,2,3,7,8]

heapsort(T)
print(T)