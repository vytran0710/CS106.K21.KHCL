#pragma once
#include <iostream>
#include <vector>
using namespace std;
class Graph
{
	int v;
	vector<int>* adj;
public:
	Graph(int v);
	void addEdge(int src, int dest);
	bool BFS(Graph g, int src, int dest, int pred[], int dist[]);
	int getVerticles();
};

