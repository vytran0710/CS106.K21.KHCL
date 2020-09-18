#include "Graph.h"
#include <list>
#include <queue>
using namespace std;
Graph::Graph(int v)
{
	this->v = v;
	adj = new vector<int>[v];
}
void Graph::addEdge(int src, int dest)
{
	adj[src].push_back(dest);
    adj[dest].push_back(src);
}
bool Graph::BFS(Graph g, int src, int dest, int pred[], int dist[])
{

    list<int> queue;

    bool* visited = new bool[g.v];

    for (int i = 0; i < v; i++) {
        visited[i] = false;
        dist[i] = INT_MAX;
        pred[i] = -1;
    }

    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);

    while (!queue.empty()) {
        int u = queue.front();
        queue.pop_front();
        for (int i = 0; i < adj[u].size(); i++) {
            if (visited[adj[u][i]] == false) {
                visited[adj[u][i]] = true;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.push_back(adj[u][i]);
                if (adj[u][i] == dest)
                    return true;
            }
        }
    }
    return false;
}
int Graph::getVerticles()
{
    return v;
}
