import DLS
def ids(G,s,t):
    limit = 1
    while True:
        parent,path,found = DLS.dls(G,s,limit,t)
        if found or limit >= len(G):
            return parent,path,found,limit,t
        limit += 1

if __name__ == "__main__":
    G = [[1,2],[3],[5],[4],[],[]]
    parent,path,found,limit,number = ids(G,0,5)
    print("parent",parent,"path",path,"number",number,"found",found,"limit",limit)