from zad3testy import runtests


def partition(T, p, k):
    q = (p+k)//2
    T[q], T[k] = T[k], T[q]
    x = T[k]
    i = p-1
    for j in range(p, k):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[k], T[i+1] = T[i+1], T[k]
    return i+1


def quick_sort(T, p, k):
    while p < k:
        q = partition(T, p, k)
        quick_sort(T, p, q-1)
        p = q+1


def strong_string(T):
    n = len(T)
    for i in range(n):
        temp = T[i][::-1]
        if temp > T[i]:
            T[i] = temp
    quick_sort(T, 0, n-1)
    res = temp = 1
    for i in range(1, n):
        if T[i] == T[i-1]:
            temp += 1
        else:
            if temp > res:
                res = temp
            temp = 1
    return max(res, temp)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
