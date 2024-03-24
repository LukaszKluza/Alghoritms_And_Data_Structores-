from math import inf 

time = 0 

def dfs(G, ART, LOW, D, v):
    global time
    children = 0

    time += 1
    LOW[v] = time
    D[v] = time 
    for x in G[v]:
        if D[x] is None:
            children += 1
            dfs(G, ART, LOW,D, x)

            if LOW[x] >= D[v]:
                ART[v] = True
            LOW[v] = min(LOW[v],LOW[x]) 
        else:
            LOW[v] = min(LOW[v],D[x]) 

    return children


def solve(G):
    global time 
    n = len(G)
    ART = [False for _ in range(n)]
    LOW = [None for _ in range(n)] 
    D = [None for _ in range(n)] 
    for i in range(n):
        if D[i] is None:
            temp = dfs(G,ART, LOW, D, i )
            print("T: ",temp)
            if temp > 1:
               ART[i] = True 
            else:
                print(i)
                ART[i] = False 
       
   
    print(len(G[0]))
    print(LOW)
    print(D)
    print(ART)

    res = 0
    for i in range(n):
        if ART[i] == True:
            print(i)

    return res


G = [[1, 3], [0, 2, 3], [1, 4], [0, 1], [2]]
print(solve(G))