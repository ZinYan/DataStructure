'''
def addEdge(adj,u,v):
    adj[u].append(v)

def displayAdjList(adj):
    print("Adjacency List Representation: ")
    for i in range(len(adj)):
        print(i,end=": ")
        for j in adj[i]:
            print(j,end=" ")
        print()

def main():
    # Create a graph with 3 vertices and 3 edges
    V = 3 #vertices
    AdjList = [[] for _ in range(V)]
    addEdge(AdjList,1,0)
    addEdge(AdjList,1,2)
    addEdge(AdjList,2,0)
    displayAdjList(AdjList)


# Directed & Unweighted
if __name__ == "__main__":
    main()

def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)    
def displayAdjList(adj):
    print("Adjacency List Representation: ")
    for i in range(len(adj)):
        print(i,end=": ")
        for j in adj[i]:
            print(j,end=" ")
        print()
def main():
    V = 3
    AdjList = [[] for _ in range(V)]
    addEdge(AdjList,1,0)
    addEdge(AdjList,1,2)
    addEdge(AdjList,2,0)
    displayAdjList(AdjList)
# Undirected & Unweighted
if __name__ == "__main__":
    main()


def addEdge(adj,u,v,w):
    adj[u].append((v,w))
def displayAdjList(adj):
    print("Adjacency List Representation: ")
    for i in range(len(adj)):
        print(i,end=": ")
        for j in adj[i]:
            print(f'{{{j[0]},{j[1]}}}',end=" ")
        print()
def main():
    V = 3
    AdjList = [[] for _ in range(V)]
    addEdge(AdjList,1,0,4)
    addEdge(AdjList,1,2,3)
    addEdge(AdjList,2,0,1)
    displayAdjList(AdjList)
# Directed & Weighted
if __name__ == "__main__":
    main()
'''
def addEdge(adj,u,v,w):
    adj[u].append((v,w))
    adj[v].append((u,w))
def displayAdjList(adj):
    print("Adjacency List Representation: ")
    for i in range(len(adj)):
        print(i,end=": ")
        for j in adj[i]:
            print(f'{{{j[0]},{j[1]}}}',end=" ")
        print()
def main():
    V = 3
    AdjList = [[] for _ in range(V)]
    addEdge(AdjList,1,0,4)
    addEdge(AdjList,1,2,3)
    addEdge(AdjList,2,0,1)
    displayAdjList(AdjList)
# Undirected & Weighted
if __name__ == "__main__":
    main()

