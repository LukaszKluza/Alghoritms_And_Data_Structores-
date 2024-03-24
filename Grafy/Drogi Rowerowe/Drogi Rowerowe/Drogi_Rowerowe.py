def DFS(G,v,vis_t,T_sort):
    vis_t[v] = 1 
    for w in G[v]:
        if vis_t[w] == 0:
            DFS(G,w,vis_t,T_sort)
    T_sort.append(v)

def DFS2(G,v,vis_t,idx,S):
    vis_t[v] = idx 
    for w in G[v]:
        if vis_t[w] == -1:
            S[idx].append(w)
            DFS2(G,w,vis_t,idx,S)

def solve():
    x = input().split()
    n = int(x[0])
    m = int(x[1])
    G = [[] for _ in range(n+1)]
    G_r = [[] for _ in range(n+1)] 
    for _ in range(m): 
        x = input().split()
        a = int(x[0])
        b = int(x[1])
        G[a].append(b)
        G_r[b].append(a)
    T_sort = [] 
    vis_t = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        if vis_t[i] == 0:
            DFS(G,i,vis_t,T_sort)
    vis_t = [-1 for _ in range(n+1)]
    T_sort.reverse()
    idx = 0
    S =[]
    for w in T_sort:
        if vis_t[w] ==-1:
            S.append([w])
            DFS2(G_r,w,vis_t,idx,S)
            idx += 1
    GS = [[] for _ in range(idx)]
    for v in range(1,n+1):
        for w in G[v]:
            if vis_t[v] != vis_t[w]:
                GS[vis_t[v]].append(vis_t[w]) 
    vis_d = [0]*idx
    D = []
    #print(GS)
    for i in range(idx):
        if vis_d[i] == 0:
                DFS(GS,i,vis_d,D)
    res = [0]*idx
    for w in D:
        res[w]+= len(S[w])
        for x in GS[w]:
            res[w]+= res[x]
    #print(D,vis_d)
    #print(res)
    for i in range(1,n+1):
        print(res[vis_t[i]]-1)

solve()