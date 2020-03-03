#include<iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		vector<int> num;
		vector<int> trash;
		bool tr = false;
		int N, inum, cnt = 0, price = 0;
		cin >> N;
		int input = 0;
		for (int i = 0; i < N; i++) {
			cin >> inum;
			num.push_back(inum);
		}
		for (int i = 1; i < N; i++) {
			if (i == N - 1) {
				if (num[i - 1] < num[i]) {
					price += num[i - 1];
					cnt++;

					input += num[i] * cnt - price;
					price = 0; cnt = 0;
				}
				continue;
			}
			if (num[i - 1] <= num[i]) {
				price += num[i - 1];
				cnt++;
				if (trash.size() > 0) {
					for (int j = 0; j < trash.size(); j++) {
						if (num[i] >= trash[j]) {
							price += trash[j];
							cnt++;
							trash[j] = 10001;
						}
					}
				}
			}
			else {
				if (price == 0 & cnt == 0) {
					trash.push_back(num[i - 1]);
				}
				else {
					input += (num[i-1] * cnt) - price;
					price = 0; cnt = 0;
				}
			}
		}
		cout << "#" << test_case << " " << input << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
