#include <iostream> 
#include <queue>
#include <list>
#include "QItem.h"
#include "Graph.h"

using namespace std;
#define N 10
#define M 10

void printShortestDistance(Graph g, int s, int dest)
{
    int* pred = new int[g.getVerticles()];
    int* dist = new int[g.getVerticles()];

    if (g.BFS(g, s, dest, pred, dist) == false)
    {
        cout << "Given source and destination"
            << " are not connected";
        return;
    }

    vector<int> path;
    int crawl = dest;
    path.push_back(crawl);
    while (pred[crawl] != -1) {
        path.push_back(pred[crawl]);
        crawl = pred[crawl];
    }

    cout << "Path with least nodes: "
        << dist[dest];

    cout << "\nPath:\n";
    for (int i = path.size() - 1; i >= 0; i--)
        cout << path[i] << " ";
}

void markIslands(char grid[N][M])
{
    int numberOfIslands = 0;
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            if (grid[i][j] == 'i')
            {
                ++numberOfIslands;
                grid[i][j] = numberOfIslands+48;
            }
        }
    }
}
int toInt(char a)
{
    return a - 48;
}
char toChar(int a)
{
    return a + 48;
}
void connectIslands(char grid[N][M], Graph&g, QItem source)
{
    bool visited[N][M];
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            visited[i][j] = false;
        }
    }
    queue<QItem> q;
    q.push(source);
    visited[source.row][source.col] = true;
    while (!q.empty()) {
        QItem p = q.front();
        q.pop();

        if (grid[p.row][p.col] != '*')
        {
            if (toInt(grid[source.row][source.col]) != toInt(grid[p.row][p.col]))
            {
                g.addEdge(toInt(grid[source.row][source.col]), toInt(grid[p.row][p.col]));
            }

            cout << toInt(grid[source.row][source.col]) << " " << toInt(grid[p.row][p.col]) << " ";

            cout << "(" << p.row << ", " << p.col << ")" << " ";
        }

        // moving up 
        if (p.row - 1 >= 0 && visited[p.row - 1][p.col] == false && p.dist < 5) //p.dist < 5 means distance has to be lower than 5 or else the ship runs out of fuel
        {
            q.push(QItem(p.row - 1, p.col, p.dist + 1));
            visited[p.row - 1][p.col] = true;
        }

        // moving down 
        if (p.row + 1 < N && visited[p.row + 1][p.col] == false && p.dist < 5)
        {
            q.push(QItem(p.row + 1, p.col, p.dist + 1));
            visited[p.row + 1][p.col] = true;
        }

        // moving left 
        if (p.col - 1 >= 0 && visited[p.row][p.col - 1] == false && p.dist < 5)
        {
            q.push(QItem(p.row, p.col - 1, p.dist + 1));
            visited[p.row][p.col - 1] = true;
        }

        // moving right 
        if (p.col + 1 < M && visited[p.row][p.col + 1] == false && p.dist < 5)
        {
            q.push(QItem(p.row, p.col + 1, p.dist + 1));
            visited[p.row][p.col + 1] = true;
        }
    }
}
void main()
{
    Graph g(8);
    char grid[N][M] =
    {
        { '0', '*', '*', '*', '*', 'i', '*', '*', '*', '*' },
        { '*', 'i', '*', '*', '*', '*', '*', '*', '*', '*' },
        { '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' },
        { '*', '*', '*', 'i', '*', '*', '*', '*', '*', '*' },
        { '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' },
        { '*', '*', 'i', '*', '*', '*', '*', '*', '*', '*' },
        { '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' },
        { '*', '*', '*', '*', 'i', '*', '*', '*', 'i', '7' },
        { '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' },
        { '*', '*', '*', '*', '*', '*', '*', '*', '*', '*' }
    };
    markIslands(grid);
    cout << "\n";
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            cout << grid[i][j] << "|";
        }
        cout << "\n";
    }
    QItem i0(0, 0, 0);
    connectIslands(grid, g, i0);

    cout << "\n";

    QItem i1(0, 5, 0);
    connectIslands(grid, g, i1);

    cout << "\n";

    QItem i2(1, 1, 0);
    connectIslands(grid, g, i2);

    cout << "\n";

    QItem i3(3, 3, 0);
    connectIslands(grid, g, i3);

    cout << "\n";

    QItem i4(5, 2, 0);
    connectIslands(grid, g, i4);

    cout << "\n";

    QItem i5(7, 4, 0);
    connectIslands(grid, g, i5);

    cout << "\n";

    QItem i6(7, 8, 0);
    connectIslands(grid, g, i6);

    cout << "\n";

    QItem i7(7, 9, 0);
    connectIslands(grid, g, i7);

    cout << "\n";

    printShortestDistance(g, 0, 7);
}

//https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
//https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/?fbclid=IwAR2YQz_v8AisP0lMPn-NPYHG0KqoMcLoCLpv5G7WUzQRnBqPIS_87Kbtjnk