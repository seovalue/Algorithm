//백준 11047번: https://www.acmicpc.net/problem/11047

#include <iostream>
using namespace std;
int arr[10];
int main(void) {
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	int sum = 0;
	for (int i = n-1; i >= 0; i--) {
		if (arr[i] > k) continue;

		int j = k / arr[i];
		sum += j;
		k = k % arr[i];
	}

	cout << sum << "\n";
	return 0;
}
