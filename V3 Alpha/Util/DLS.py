found = False
def dls(G,s,l,t):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    path = []
    values = []
    def _dfs(G,u,l,t):
        if l == 0:
            return
        if u == t:
            global found
            found = True
        if not visited[u]:
            visited[u] = True
            path.append(u)
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                _dfs(G,v,l-1,t)
    
    _dfs(G,s,l,t)
    return parent,path,found

if __name__ == "__main__":
    G = [[1,2],[3],[5],[4],[],[]]
    parent,path,found = dls(G,0,4,4)
    print("parent",parent,"path",path,"found",found)