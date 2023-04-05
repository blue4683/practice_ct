#include <iostream>

using namespace std;

int T, A, B, R;

int GCM(int a, int b) {
	if (b > a)
		b, a = a, b;
	while (1) {
		int r = b % a;
		if (r == 0) return a;
		b = a;
		a = r;
	}
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		R = A * B / GCM(A, B);
		cout << R << '\n';
	}
}