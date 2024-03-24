from zad6ktesty import runtests 

def haslo ( S ):
    n = len(S)
    DP = [0]*n
    if S == '':
        return 1
    for i in range(n):
        if S[i] == '0':
            if i == 0 or (S[i-1] != '1' and S[i-1] != '2'):
                return 0
    DP[0] = 1
    temp = int(S[0])*10+int(S[1])
    if temp <27:
        DP[1] = 2
    else: DP[1] = 1
    for i in range(2,n):
        temp = int(S[i-1]) * 10 + int(S[i])
        if S[i] == '0':
            DP[i] = DP[i-2]
        elif 10 < temp < 27:
            DP[i] = DP[i-1]+DP[i-2]
        else: DP[i] = DP[i-1]
    return DP[n-1]

runtests ( haslo )