//백준 2675번: https://www.acmicpc.net/problem/2675
#include <iostream>
#include <string>
using namespace std;
int main(void) {
	int t, n;
	cin >> t;
	string str;
	for (int i = 0; i < t; i++) {
		cin >> n >> str;
		for (int i = 0; i < str.size(); i++) {
			for (int j = 0; j < n; j++) {
				cout << str[i];
			}
		}cout << "\n";
	}

	return 0;
}
