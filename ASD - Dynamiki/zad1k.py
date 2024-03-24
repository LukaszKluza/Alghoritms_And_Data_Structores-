from zad1ktesty import runtests

def f(S, T, a, b):
    if T[a][b]:
        return T[a][b]
    if a == b:
        if S[a] == '1':
            T[a][b] = -1
            return -1
        T[a][b] = 1
        return 1
    if S[b] == '1':
        T[a][b] = f(S,T,a,b-1)-1
    else:
        T[a][b] = f(S,T,a,b-1)+1
    return T[a][b]

def roznica( S ):
    n = len(S)
    res = -1
    T = [[0 for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(a+1,n):
            T[a][b] = f(S,T,a,b)
            res = max(T[a][b], res)
    return res

runtests ( roznica )