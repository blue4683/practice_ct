#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = -1e9;

int n, k;
vector<int> chess;
vector<vector<vector<int>>> dp;

int cover(int idx, int status, int cnt)
{
    if (cnt == 0)
        return 0;
    if (idx >= n * 3)
        return INF;

    int &ret = dp[idx][status][cnt];

    if (ret != INF)
        return ret;

    if (status & 1)
        ret = cover(idx + 1, status >> 1, cnt);
    else
    {
        ret = cover(idx + 1, status >> 1, cnt);

        if (idx + 3 < n * 3)
            ret = max(ret, cover(idx + 1, status >> 1 | 4, cnt - 1) + chess[idx] + chess[idx + 3]);

        if (idx % 3 != 2 && !(status & 2))
            ret = max(ret, cover(idx + 2, status >> 2, cnt - 1) + chess[idx] + chess[idx + 1]);
    }

    return ret;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    chess.resize(n * 3);
    dp.resize(3 * (n + 1), vector<vector<int>>(8, vector<int>(k + 1, INF)));

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            int val;
            cin >> val;
            chess[i * 3 + j] = val;
        }
    }

    cout << cover(0, 0, k) << endl;

    return 0;
}
