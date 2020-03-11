#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
int get_gcd(int a, int b) {
	if (b == 0) return a;
	else
		return get_gcd(b, a%b);
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		string str;
		cin >> str;
		vector<char> vec;
		int i = 0;
		while (true) {
			if (i >= str.size()) break;
			if (str[i] == 'n') {
				vec.push_back('n');
				i += 5;
			}
			if (str[i] == 'w') {
				vec.push_back('w');
				i += 4;
			}
		}
		double a;
		int n = 1;
		if (vec[vec.size() - 1] == 'w') {
			a = 90;
		}
		else {
			a = 0;
		}

		string res = "";
		double tmp;
		for (int i = vec.size() - 2; i > 0; i--) {
			tmp = pow(2, n);
			if (vec[i] == 'w') {
				a = a + 90 / tmp;
			}
			else {
				a = a - 90 / tmp;
			}
			n++;
		}
		if (vec.size()>1) {
			int tmp1;
			tmp = pow(2, n);
			if (vec[0] == 'w') {
				tmp1 = tmp * a + 90;
				a = a + 90 / tmp;
				if (floor(a) < a) { //소수자리가 존재한다면
					int gcd = get_gcd(tmp1, tmp);
					res += to_string(tmp1 / gcd);
					res += "/";
                    int base = tmp/gcd;
					res += to_string(base);
				}
			}
			else {
				tmp1 = tmp * a - 90;
				a = a - 90 / tmp;
				if (floor(a) < a) { //소수자리가 존재한다면
					int gcd = get_gcd(tmp1, tmp);
					res += to_string(tmp1 / gcd);
					res += "/";
                    int base = tmp/gcd;
					res += to_string(base);
				}
			}
		}


		if (res.size() != 0)
			cout << "#" << test_case << " " << res << "\n";
		else
			cout << "#" << test_case << " " << a << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
