from zad3ktesty import runtests
from math import inf

def f(T,DP,x,k):
    if DP[x] != inf:
        return DP[x]
    if x<k:
        DP[x] = T[x]
        return DP[x]
    for i in range(x-k,x):
        DP[x] = min(DP[x], f(T,DP,i,k))
    DP[x] += T[x]
    return DP[x]

def ksuma( T, k ):
    n = len(T)
    DP = [inf]*n
    for i in range(n):
        DP[i] = f(T,DP,i,k)
    res = DP[n-1]
    for i in range(n-k,n):
        res = min(DP[i], res)
    return res
    
runtests ( ksuma )