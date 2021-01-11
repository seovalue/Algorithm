#include<iostream>
#include <algorithm>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int p,q,r,s,w;
        cin >> p >> q >> r >> s >> w;
        int fee_A = w * p;
        int fee_B;
        if( w > r ){
            fee_B = (w - r) * s + q;
        } else
            fee_B = q;

        int fee = min(fee_A, fee_B);
        printf("%s%d %d\n", "#", test_case, fee);
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
