#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int N;
string R;
int arr[int(1e6) + 5001];
vector<int> P;

int main() {
	cin >> N;
	arr[int(1e6) + 1] = { 0, };
	for (int i = 2; i <= int(1e6) + 5000; i++) {
		if (arr[i] == 1) continue;
		P.push_back(i);
		int j = 2;
		while (i * j <= int(1e6) + 5000) {
			arr[i * j] = 1;
			j++;
		}
	}
	for (int i : P) {
		if (i < N) continue;
		string num = to_string(i);
		int flag = 1;
		for (int j = 0; j < (num.size() / 2); j++) {
			if (num[j] != num[num.size() - j - 1]) flag = 0;
		}
		if (flag == 1) {
			R = num;
			break;
		}
	}
	cout << R << '\n';
	return 0;
}