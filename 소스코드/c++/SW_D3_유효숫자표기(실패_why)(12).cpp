#include<iostream>
#include<cmath>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		double n;
        int cnt = 1;
        cin >> n;
        while(true){
            if(n < 100) break;
            cnt++;
            n /= 10;
        }
        n = round(n) / 10;

        if(n == 10){
            cnt++;
            n /= 10;
        }
        printf("%s%d %.1f%s%d\n", "#",test_case,n,"*10^",cnt);
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
