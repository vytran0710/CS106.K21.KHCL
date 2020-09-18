from collections import defaultdict 
class Graph: 
  
    def __init__(self,vertices): 
        self.V = vertices 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def DLS(self,src,target,maxDepth): 
        if src == target : return True
        if maxDepth <= 0 : return False
        for i in self.graph[src]: 
                if(self.DLS(i,target,maxDepth-1)): 
                    return True

        return False
    def IDDFS(self,src, target, maxDepth): 
        for i in range(maxDepth): 
            if (self.DLS(src, target, i)): 
                return True
        return False
g = Graph (10); 
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(3, 7)
g.addEdge(4, 8)
g.addEdge(5, 9)

  
target = 0; maxDepth = 1; src = 0
  
if g.IDDFS(src, target, maxDepth) == True: 
    print ("Found target within max depth") 
else : 
    print ("Not Found target within max depth") 
  


#Tham khao: https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/