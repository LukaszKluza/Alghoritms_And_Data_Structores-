from zad6testy import runtests
from collections import deque


def bfs(graph, pair_u, pair_v, dist):
    queue = deque()
    for u in range(len(graph)):
        if pair_u[u] == -1:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')

    dist[-1] = float('inf')

    while queue:
        u = queue.popleft()
        if dist[u] < dist[-1]:
            for v in graph[u]:
                #print(v,pair_v)
                if dist[pair_v[v]] == float('inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])

    return dist[-1] != float('inf')

def dfs(graph, pair_u, pair_v, dist, u):
    if u == -1:
        return True

    for v in graph[u]:
        if dist[pair_v[v]] == dist[u] + 1 and dfs(graph, pair_u, pair_v, dist, pair_v[v]):
            pair_u[u] = v
            pair_v[v] = u
            return True

    dist[u] = float('inf')
    return False

def hopcroft_karp(graph):
    pair_u = [-1] * len(graph)
    pair_v = [-1] * len(graph)
    dist = [-1] * (len(graph) + 1)
    matching = 0

    while bfs(graph, pair_u, pair_v, dist):
        for u in range(len(graph)):
            if pair_u[u] == -1 and dfs(graph, pair_u, pair_v, dist, u):
                matching += 1

    return matching

def binworker(M):
    n = len(M)
    G = [[] for _ in range(2*n)]
    for i in range(n):
        for v in M[i]:
            G[i+n].append(v)
            G[v].append(i+n)

    res = hopcroft_karp(G)
    #print("Res ",res)
    return res//2

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )


M = [
    [0, 1, 3],
    [2, 4],
    [0, 2],
    [3],
    [3, 2]
]

