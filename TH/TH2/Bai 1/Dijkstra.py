from collections import defaultdict 

class Graph: 
	def minDistance(self,dist,queue): 
		
		minimum = float("Inf") 
		min_index = -1
		for i in range(len(dist)): 
			if dist[i] < minimum and i in queue: 
				minimum = dist[i] 
				min_index= i
		return min_index 
	def printPath(self, parent, j): 
		if parent[j] == -1 : 
			print (j), 
			return
		self.printPath(parent , parent[j]) 
		print (j), 
	def printSolution(self, dist, parent,src,goal): 
			print("%d -->  \t%d \t\t\t" % (src, goal)),
			self.printPath(parent,goal)
	def dijkstra(self, graph, src,goal): 
		row = len(graph) 
		col = len(graph[0]) 
		dist = [float("Inf")] * row 
		parent = [-1] * row 
		dist[src] = 0
		queue = [] 
		for i in range(row): 
			queue.append(i)  
		while queue: 
			u = self.minDistance(dist,queue) 	 
			queue.remove(u) 
			for i in range(col): 
				if graph[u][i] and i in queue: 
					if dist[u] + graph[u][i] < dist[i]: 
						dist[i] = dist[u] + graph[u][i] 
						parent[i] = u 
		self.printSolution(dist,parent,src,goal) 

g= Graph() 		
graph = [[0, 7, 0, 0, 3, 0, 0, 0, 0,0], 
		 [7, 0, 5, 10, 0, 2, 0, 0, 0,0], 
		 [0, 5, 0, 0, 0, 0, 7, 0, 0,0], 
		[0, 10, 0, 0, 0, 0, 0, 0, 4,0], 
		[3, 0, 0, 0, 0, 0, 0, 0, 0,5], 
		[0, 2, 0, 0, 0, 0, 12, 0, 0,0], 
		[0, 0, 7, 0, 0, 0, 0, 10, 0,0], 
		[0, 0, 0, 0, 0, 0, 10, 0, 12,9], 
		[0, 0, 0, 4, 0, 0, 0, 12, 0,0], 
		[0, 0, 0, 0, 5, 0, 0, 9, 0,0] 
		] 


src = int(input("Nhap src = "))
Goal = int(input("Nhap goal = "))
g.dijkstra(graph,src,Goal) 



