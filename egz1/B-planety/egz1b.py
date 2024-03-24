'''
Lukasz Kluza
rozwazam sobie fukncje f(i,b) ktora mowi jaki jest minimalny koszt przybycia na planete 'i' i posiadanie 'b' paliwa
(najpierw zakladam, ze nie ma telepoertow)
Aby dotrzec do planety 'i' to moglem tam dojsc tylko z planety 'i-1' ( i > 0), wiec dla kazdej planaty 'i' rozwazam
wszystkie mozeliwe oplcje tankowania(w tablicy DP[i][b] zapisuje minimalny koszt posiadania na planecie 'i', 'b' paliwa w baku )
tj. minimalnie na planecie 'i' musialem zatankowac tyle paliwa aby dostac sie na planete 'i' a maksymalnie w baku na
placenie i moge miec paliwo z planety 'i-1' - koszt krawedzi z 'i-1' do 'i' + paliwo zatankowane na planecie 'i' co
musi byc <= od pojemnosci baku.

(rozwazam uzycie teleportu)
Dla kazdej planety wiem z jakiej innej mogelem sie do niej dostac, wiem tez ze uzywajac na planecie 'j' teleportu do 'i'
bede na placecie 'i' z pustym bakiem wiec rozwazam ze na planecie 'i' moge zatankowac od 1 do E paliwa oraz do kosztu
doliczam 'p' czyli kosztu uzycia teleportu

Zlozonosc O(nE^3)
'''

from egz1btesty import runtests
from math import inf


def f(planet, fuel, E, DP, C, T,D):
    if DP[planet][fuel] != inf:
        return DP[planet][fuel]
    if planet == 0:
        DP[planet][fuel] = fuel * C[0]
        return DP[planet][fuel]
    for i in range(E+1):            # opcja gdzie nie uzywam teleportow
        for j in range(E+1):
            cost = D[planet]-D[planet-1]
            if 0 <= i - cost and i - cost + j <= E:          # na poprzedniej planecie musialem miec minium tyle paliwa aby doleciec to tej, ale w sumie na tej nie moge miec wiecej niz ma bak
                DP[planet][i+j-cost] = min(DP[planet][i+j-cost], f(planet - 1, i, E, DP, C, T, D) + C[planet] * j)
    for i in range(E+1):    # uzywam teleportu
        if len(T[planet]) > 0:
            for j, p in T[planet]:
                DP[planet][i] = min(DP[planet][i], f(j, 0, E, DP, C, T, D) + p + C[planet] * i)
    return DP[planet][fuel]


def planets( D, C, T, E ):
    n = len(D)
    res = inf
    DP = [[inf for _ in range(E+1)] for _ in range(n)]
    Teleports = [[] for _ in range(n)]
    for i in range(D[1]):
        DP[0][i] = i * C[0]
    for i in range(n):
        j, p = T[i]
        if i != j:
            Teleports[j].append([i, p])
    for i in range(E+1):
        f(n-1, i, E, DP, C, Teleports, D)
    for i in range(E+1):
        res = min(res, DP[n-1][i])
    return DP[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
