#include<iostream>
#include<algorithm>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int n; cin >> n;
        int seat[n];
        for(int i = 0; i < n; i++) cin >> seat[i];
        sort(seat,seat+n);
        int sum = 0;
        for(int i = 0; i < n; i++){
            sum += seat[i];
        }
        sum += seat[n-1] + n;

        printf("%s%d %d\n","#",test_case,sum);

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
