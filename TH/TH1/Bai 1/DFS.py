Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import defaultdict
>>> class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	def addEdge(self, u, v):
		self.graph[u].append(v)
	def DFSs(self, v, visited):
		visited[v]=True
		print(v, end=' ')
		for i in self.graph[v]:
			if visited[i]== False:
				self.DFSs(i, visited)
	def DFS(self, v):
		visited=[False]*(len(self.graph))
		self.DFSs(v, visited)

>>> g=Graph()
>>> g.addEdge(0, 1)
>>> g.addEdge(0, 2)
>>> g.addEdge(1, 4)
>>> g.addEdge(2, 3)
>>> g.addEdge(3, 5)
>>> g.addEdge(4, 5)
>>> g.addEdge(2, 6)
>>> g.addEdge(6, 7)
>>> g.addEdge(7, 5)
>>> g.addEdge(5, 7)
>>> g.addEdge(1, 6)
>>> print("start from 0: ")
start from 0: 
>>> g.DFS(0)
0 1 4 5 7 6 2 3 
>>> 