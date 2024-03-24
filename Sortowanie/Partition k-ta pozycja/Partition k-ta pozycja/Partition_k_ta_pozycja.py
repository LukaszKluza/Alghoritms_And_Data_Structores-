def partition(T,p,k):
    q = (p+k)//2
    T[q],T[k] = T[k], T[q] 
    x = T[k]
    i = p-1
    for j in range(p,k):
        if T[j] <= x:
            i+=1
            T[i],T[j]=T[j],T[i] 
    T[i+1],T[k] = T[k],T[i+1]
    return i+1

def select(T,p,k,x):
    res = partition(T,p,k)
    if res == x:
        return T[x] 
    if res < x:
        return select(T,res+1,k,x)
    return select(T,0,res-1,x)


T = [4,8,1,3,2,0,6]
for i in range(len(T)):
    print(select(T,0,len(T)-1,i))



