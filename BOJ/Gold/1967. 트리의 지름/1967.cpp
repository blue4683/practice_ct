#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

void BFS(int start, vector<vector<pair<int, int>>> &arr, int visited[10001])
{
    queue<int> Q;
    Q.push(start);
    visited[start] = 1;

    while (!Q.empty())
    {
        int now = Q.front();
        Q.pop();

        for (auto info : arr[now])
        {
            int next = info.first;
            int weight = info.second;

            if (visited[next] == 0)
            {
                visited[next] = visited[now] + weight;
                Q.push(next);
            }
        }
    }
}

int main()
{
    int n;
    cin >> n;
    vector<vector<pair<int, int>>> arr(10001);

    for (int i = 0; i < n - 1; i++)
    {
        int y, x, w;
        cin >> y >> x >> w;
        arr[y].push_back({x, w});
        arr[x].push_back({y, w});
    }

    int visited[10001] = {0};

    BFS(1, arr, visited);

    int maxNode = 1;

    for (int i = 1; i <= n; i++)
    {
        if (visited[i] > visited[maxNode])
        {
            maxNode = i;
        }
    }

    fill(visited, visited + 10001, 0);

    BFS(maxNode, arr, visited);

    int result = *max_element(visited, visited + 10001);

    cout << result - 1 << "\n";

    return 0;
}