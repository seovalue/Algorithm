#include<iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int n;
        long long dist;
        cin >> n;
        long long d[n];
        for(int i = 0; i < n; i++){
            cin >> dist;
            d[i] = abs(dist);
        }
        sort(d,d+n);
        int min = d[0], cnt = 0;
        for(int i = 0; i < n; i++){
            if(min == d[i]) cnt++;
        }
        printf("%s%d %d %d\n","#",test_case,min,cnt);
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
