#include <iostream>
#include <cmath>

using namespace std;

long long MIN, MAX, R;
int arr[int(1e6) + 1];

int main() {
	cin >> MIN >> MAX;
	R = 0;
	arr[int(1e6) + 1] = { 0, };
	for (long long i = 2; i < sqrt(MAX) + 1; i++) {
		long long P = i * i;
		long long S = MIN / P;
		if (MIN % P != 0) S++;
		for (long long j = S; j < (MAX / P) + 1; j++) {
			arr[j * P - MIN] = 1;
		}
	}
	for (int i = 0; i <= MAX - MIN; i++) {
		if (arr[i] == 0) R++;
	}
	cout << R << '\n';
	return 0;
}