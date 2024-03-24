from zad10ktesty import runtests
from math import inf,sqrt

def dywany ( N ):
    print(N)
    res = []
    T = [inf]*(N+1)
    P = [0]*(N+1)
    n = int(sqrt(N))
    T[0] = 0
    for i in range(1,n+1):
        for j in range(i*i,N+1):
            if T[j-i*i] + 1 < T[j]:
                T[j] = min(T[j], T[j - i * i] + 1)
                P[j] = j-i*i
    temp = P[N]
    idx = N
    while idx:
        pole = idx - temp
        res.append(int(sqrt(pole)))
        idx = temp
        temp = P[idx]
    return res


runtests( dywany )

