#include <iostream>
#include <stack>
using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n, num;
		long long result = 0, max = 0;
		stack<int> price;
		cin >> n;
		for (int j = 1; j <= n; ++j) {
			cin >> num;
			price.push(num);
		}
		max = price.top();
		while (!price.empty()) {
			int top = price.top();
			price.pop();

			if (max < top) max = top;
			result += max - top;
		}
		cout << "#" << i + 1 << " " << result << "\n";
	}
	return 0;
}
