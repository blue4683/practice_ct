#include <bits/stdc++.h>

#define Y first
#define X second

using namespace std;

int N, M;
int sy, sx;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    int arr[N][M] = {};
    int visited[N][M] = {};
    queue<pair<int, int>> Q;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 2)
            {
                sy = i;
                sx = j;
            }
        }
    }
    Q.push({sy, sx});

    while (!Q.empty())
    {
        pair<int, int> cur = Q.front();
        Q.pop();
        int y = cur.Y;
        int x = cur.X;

        for (int dir = 0; dir < 4; dir++)
        {
            int yy = y + dy[dir];
            int xx = x + dx[dir];

            if (yy < 0 || yy >= N || xx < 0 || xx >= M)
            {
                continue;
            }
            if (arr[yy][xx] != 1 || visited[yy][xx])
            {
                continue;
            }

            visited[yy][xx] = visited[y][x] + 1;
            Q.push({yy, xx});
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (!visited[i][j] && arr[i][j] == 1)
            {
                cout << -1 << ' ';
            }
            else
            {
                cout << visited[i][j] << ' ';
            }
        }
        cout << '\n';
    }
    return 0;
}