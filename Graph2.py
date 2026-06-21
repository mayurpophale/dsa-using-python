#Implementation of graph using adjacency list

class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}
    
    def add_edge(self,u,v,wei=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,wei))
            self.adj_list[v].append((u,wei))
        else: 
            print("Invalid")
    
    def remove(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u] = [(v,wei) for vertex,wei in self.adj_list[u] if vertex !=v ]
            self.adj_list[v] = [(u,wei) for vertex,wei in self.adj_list[v] if vertex !=u ]
        else:
            print("Invalid")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex, x in self.adj_list[u])
        else:
            return False
    
    def print_list(self):
        for vertex,n in self.adj_list.items():
            print("V",vertex,":",n)
        

g = Graph(5)
g.add_edge(2,3)
g.add_edge(0,1)
g.add_edge(4,2)
g.add_edge(4,8)
g.add_edge(1,3)
g.print_list()
