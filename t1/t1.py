
#Nome:Augusto Sacramento Rodrigues RA:213368

def eh_seq_grafica(d):
    
    for i in range(len(d)):
        d1=d[i]
        if d1 > len(d[i+1:]): return False
        for j in range(1,d1+1):
            d[i+j]-=1
        d[i+1:]=sorted(d[i+1:],reverse=True)
        if d[-1]<0: return False  
   
    return True

def monta_grafo(d):
    #Lista de adjacencia
    grafo = [[] for _ in range(len(d))]
    # i = indece do vertice j = grau do vertice
    v = [[i,j] for i,j in enumerate(d)]
    
    for i in range(len(v)-1):
        j=i+1
        while v[i][1]>0:
            if v[j][1]>0:
                grafo[v[i][0]].append(v[j][0]+1)
                grafo[v[j][0]].append(v[i][0]+1)
                v[i][1]-=1
                v[j][1]-=1
            #else: break
            j+=1
        v[i+1:] = sorted(v[i+1:],key=lambda x:x[1],reverse=True)
    return grafo

def main():
    
    _ = int(input())
    d = list(map(int,input().split()))
    if eh_seq_grafica(d.copy()):
        for i in monta_grafo(d):
            print(*i)
    else:
        print("Não é sequência gráfica!")
    


main()