def addEdge(mat,i,j):
    mat[i][j] = 1
    mat[j][i] = 1    
def displayadjMatrix(mat):
    print('Adjacency matrix Representation')
    for row in mat:
        print(" ".join(map(str,row)))
def main():
    V = 3
    # matrix with 3 vertices and 3 edges
    mat = [[0]*(V+1) for _ in range(V+1)]
    # Add edges to the graph
    addEdge(mat,0,1)
    addEdge(mat,1,2)
    addEdge(mat,2,3)
    displayadjMatrix(mat)
# Unweighted Undirected
if __name__ == '__main__':
    main()


    