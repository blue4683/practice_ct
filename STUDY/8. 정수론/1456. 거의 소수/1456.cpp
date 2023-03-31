#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

long long A, B;
int R;
const int MAX = int(1e7) + 1;
int arr[MAX];

int main() {
	cin >> A >> B;
	R = 0;
	for (int i = 2; i < int(sqrt(B)) + 1; i++) {
		if (arr[i] != 0) continue;
		for (int j = i * 2; j < MAX; j += i)
			arr[j] = 1;
	}
	for (int i = 2; i < int(sqrt(B)) + 1; i++) {
		if (arr[i] != 0) continue;
		long long j = i;
		int k = i;
		while (j <= B / k) {
			j *= k;
			if ((A <= j) && (B >= j)) {
				R++;
			}
		}
	}
	cout << R << "\n";
	return 0;
}