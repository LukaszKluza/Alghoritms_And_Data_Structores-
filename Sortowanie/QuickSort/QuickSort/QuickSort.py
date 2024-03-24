def partition(T,p,k):
    q = (p+k)//2
    T[k],T[q]=T[q],T[k]
    x = T[k]
    i = p-1
    for j in range(p,k):
        if T[j] <=x:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[k] = T[k],T[i+1]
    return i+1

def quickSort(T,p,k):
    while p < k:
        q = partition(T,p,k)
        quickSort(T,p,q-1)
        p+=q

T1 = [3,1,4,0,12,43,7,2,4,8]
T = [4,1,6,12,5,11,7]
print(partition(T1,0,len(T1)-1))
quickSort(T,0,len(T)-1)
print(T)
