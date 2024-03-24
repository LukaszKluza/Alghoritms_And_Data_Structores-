from zad2ktesty import runtests

def f(S,T,a,b):
    if T[a][b]:
        return T[a][b]
    if a == b - 1:
        if S[a] == S[b]:
            T[a][b] = True
            return True
        else:
            T[a][b] = False
            return False
    if a == b:
        T[a][b] = True
        return True
    if S[a]==S[b]:
        T[a][b] = f(S, T, a + 1, b - 1)
    else:
        T[a][b] = False
    return T[a][b]


def palindrom( S ):
    n = len(S)
    P = [[0 for _ in range(n)] for _ in range(n)]
    maxi = 0
    for a in range(n):
        for b in range(a+1,n):
            P[a][b] = f(S,P,a,b)
            if P[a][b] and b-a +1 > maxi:
                pal = S[a:b+1]
                maxi = b-a+1
    return pal
runtests ( palindrom )