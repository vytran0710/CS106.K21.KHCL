#pragma once
class QItem {
public:
    int row;
    int col;
    int dist;
public:
    QItem(int x, int y, int w)
        : row(x), col(y), dist(w)
    {
    }
};

