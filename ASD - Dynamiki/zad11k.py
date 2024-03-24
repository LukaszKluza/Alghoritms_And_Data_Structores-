from zad11ktesty import runtests

def f(T, x = 0,s1 = 0,s2 = 0):
    print(x,s1,s2)
    if x == len(T)-1:
        return T[len(T)-1]
    return min(f(T, x+1, s1+T[x], s2),
               f(T,x+1, s1, s2 + T[x]))


def kontenerowiec(T):
    print(T)
    sum_T = sum(T)

    if len(T)< 10: return abs(sum_T - 2*f(T))

runtests ( kontenerowiec )
    