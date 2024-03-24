from zad2testy import runtests

def heapify(T, i, n):
    max_int = i
    l = i*2+1
    r = l + 1
    if l < n and T[max_int] < T[l]:
        max_int = l
    if r < n and T[max_int] < T[r]:
        max_int = r
    if i != max_int:
        T[i], T[max_int] = T[max_int], T[i]
        heapify(T, max_int, n)

def snow( S ):
    n = len(S)
    for i in range((n - 2) // 2, -1, -1):
        heapify(S, i, n)
    day = res = 0
    for i in range(n - 1, 0, -1):
        if S[0] < day:
            return res - ((day - 1) * day) // 2
        res += S[0]
        day += 1
        S[i], S[0] = S[0], S[i]
        heapify(S, 0, i)
    return res - ((day + 1) * day) / 2

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
