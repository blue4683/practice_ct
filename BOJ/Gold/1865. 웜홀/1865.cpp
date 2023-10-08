#include <iostream>
#include <vector>
#include <algorithm>

#define INF 21e8

using namespace std;

struct node
{
    int s, e, t;
};

bool bellmanFord(int index, vector<node> edges)
{
    int result[index + 1];
    fill(result, result + index + 1, INF);
    result[1] = 0;
    for (int j = 0; j < index; j++)
    {
        for (node edge : edges)
        {
            if (result[edge.s] + edge.t < result[edge.e])
            {
                result[edge.e] = result[edge.s] + edge.t;
            }
        }
    }
    for (node edge : edges)
    {
        if (result[edge.s] + edge.t < result[edge.e])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++)
    {
        int n, m, w;
        cin >> n >> m >> w;

        vector<node> edges;

        for (int j = 0; j < m + w; j++)
        {
            int s, e, t;
            cin >> s >> e >> t;
            if (j >= m)
            {
                t *= -1;
            }
            edges.push_back({s, e, t});
            if (j < m)
            {
                edges.push_back({e, s, t});
            }
        }

        if (!bellmanFord(n, edges))
        {
            cout << "YES"
                 << "\n";
        }
        else
        {
            cout << "NO"
                 << "\n";
        }
    }

    return 0;
}