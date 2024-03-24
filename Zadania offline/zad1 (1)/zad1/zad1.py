from zad1testy import runtests

def ceasar( s ):
    n = len(s)
    i = 0
    t = 0
    res = 0
    T = [0 for _ in range(n) ]
    while i < n:
        while t <= i and  t >= -i and i-t < n and i+t < n and s[i-t] == s[i+t]: t += 1
        k = 1
        T[i] = t
        while k < t and T[i-k] != T[i] -k:
            T[i+k] = min(T[i-k],T[i]-k)
            res = max(T[i-k],T[i]-k)*2-1
            k+=1
        t = max(t-k, 0)
        i += k

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
