'''
Lukasz Kluza
Problem rozwiazuje etapami, w kazdym etapie rozwazam pojedyncza kolumne,
Dla kazdej kolumny analizuje czy dla danago pola bardziej oplaca sie dojsc od gory czu dolu,
(z wyjatkiem kolumny zerowej, tam da sie tylko isc w dol)
aktualizuje dane w tej kolumnie wyliczajac maxa i nastepnie jesli dana komorka w kolumnie obok jest osiagalna
to przepisuje do niej wartosc z obecnej powiekszajac ja o 1
O(n^2)
'''

from zad7testy import runtests


def maze( L ):
    n = len(L)
    if L[n-1][n-1] =="#":
        return -1
    M = [[-1 for _ in range(n)] for _ in range(n)]
    U = [[-1 for _ in range(n)] for _ in range(n)]
    D = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                M[i][j] = -2
    for i in range(n):
        if M[i][0] == -2:
            break
        else:
            M[i][0] = i
    for col in range(1, n):
        for row in range(n):
            if M[row][col] != -2 and M[row][col-1] >= 0:
                M[row][col] = M[row][col-1]+1

        for row in range(n):
            if M[row][col] != -2:
                if row != 0 and D[row-1][col] > -1:
                    D[row][col] = max(D[row - 1][col] + 1, M[row][col])
                elif row == 0 or M[row][col - 1] > -1:
                    D[row][col] = M[row][col]

        for row in range(n-1, -1, -1):
            if M[row][col] != -2:
                if row != n-1 and U[row+1][col] != -1:
                    U[row][col] = max(U[row + 1][col] + 1, M[row][col])
                elif row == n - 1 or M[row][col-1] > -1:
                    U[row][col] = M[row][col]

        for row in range(n):
            if M[row][col] > -2:
                M[row][col] = max(M[row][col], U[row][col], D[row][col])
    return M[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
