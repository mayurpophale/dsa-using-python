#Implenetion of graph using adjacency matrix(simple and undirected)
class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_matrix = [ [0]*vno for i in range(vno)] #matrix with all element 0 and size vno*vno
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invaild edgee")
        
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("invaild edgee")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invaild vertex")
    
    def print_matrix(self):
        for row in self.adj_matrix:
            print(' '.join(map(str,row)))
    
g = Graph(5)
g.add_edge(0,1)
g.add_edge(4,2)
g.add_edge(4,8)
g.add_edge(2,3)

g.print_matrix()
print(g.has_edge(1,0))