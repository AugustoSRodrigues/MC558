class grafo():
    def __init__(self,n) -> None:
        self.adj = [[] for _ in range(n)]

    def add_node(self,u,v,c):
       
        self.adj[u].append([v,c,False])
        self.adj[v].append([u,c,False])
        self.adj[u][-1].append(self.adj[v][-1])
        self.adj[v][-1].append(self.adj[u][-1])

def trilha_maximal(r,adj):
    u = r
    T = []
    T.append(u)
    while len(adj[u])>0:
        v=adj[u][0][0]
        T.append(v)
        adj[v].pop(adj[v].index(adj[u][0][-1]))
        adj[u].pop(0)
        u = v
    return T

def trilha_euler(m,adj):
    T = trilha_maximal(0,adj)
    while len(T) < m+1:
        for i,t in enumerate(T):
            if len(adj[t])>0:
                v = t
                b = i
                break
        T_linha = trilha_maximal(v,adj)
        T =T[:b]+T_linha[:-1]+T[b:] 
    return T


    
def main():
    n,m = map(int,input().split())
    graus = [0,0]
    G = grafo(n)
    
    
    for _ in range(m):
        u,v,c = map(int,input().split())
        graus[c]+=1
        G.add_node(u,v,c)
    
    
    if graus[0]%2 ==1 or graus[1]%2==1:
        print("Não possui trilha Euleriana alternante")
    else:
        e = trilha_euler(m,G.adj)
        print(*e)

main()