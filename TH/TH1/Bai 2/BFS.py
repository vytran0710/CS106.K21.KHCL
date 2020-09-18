from collections import defaultdict 
class Graph: 
    def __init__(self):  
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def BFS(self, s): 
        visited = [False] * (len(self.graph)) 
        queue = [] 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
  

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 4) 
g.addEdge(2, 3)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(2, 6)
g.addEdge(6, 7)
g.addEdge(7, 5)
g.addEdge(5, 7)
g.addEdge(1, 6)
print("BFS starts from 0: ")
g.BFS(0) 