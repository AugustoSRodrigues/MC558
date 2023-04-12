class grafo():
    def __init__(self,n) -> None:
        self.adj = [[[],[]]for _ in range(n)]
        self.arestas = [0,0]

    def add_node(self,u,v,c):
        self.adj[u][c].append(v)
        self.adj[v][c].append(u)
        # self.adj[u][c][-1].append(len(self.adj[v][c])-1)
        # self.adj[v][c][-1].append(len(self.adj[u][c])-1)
        self.arestas[c]+=1


    def eh_euler_alter(self):
        if self.arestas[0]%2 ==1 or self.arestas[1]%1==1:
            return False
        return True
    


    
        

def trilha_maximal(r,adj,flag=True):
    u = r
    T = []
    colors = []
    T.append(u)
    while True:
        c = 0 if flag else 1
        if len(adj[u][c])<=0:
            return T,colors
        v = adj[u][c][0]
        T.append(v)
        adj[v][c].pop(adj[v][c].index(u))
        adj[u][c].pop(0)
        colors.append(c)
        u = v
        flag=not flag
    

def trilha_euler(m,adj):
    T,C= trilha_maximal(0,adj)
    while len(T) < m+1:
        for i,t in enumerate(T):
            c = C[i-1]
            
            if len(adj[t][c])>0:
                v = t
                b = i
                break
        T_linha,c_linha= trilha_maximal(v,adj,c)
        T =T[:b]+T_linha[:-1]+T[b:]
        C = C[:b]+c_linha[:-1]+C[b:]
    #print(*C)
    return T


    
def main():
    n,m = map(int,input().split())
    graus = [0,0]
    G = grafo(n)

    
    for _ in range(m):
        u,v,c = map(int,input().split())
        graus[c]+=1
        G.add_node(u,v,c)
    
    if not G.eh_euler_alter():
        print("Não possui trilha Euleriana alternante")
    else:
        e = trilha_euler(m,G.adj)
        print(*e)
        
    
    # T,colors= trilha_maximal(0,G.adj)
    # print(*T)
    # print(*colors)
    # print(list(zip(T,colors)))
    # if graus[0]%2 ==1 or graus[1]%2==1:
    #     print("Não possui trilha Euleriana alternante")
    # else:
    # e = trilha_euler(m,G.adj)
    # print(*e)

main()