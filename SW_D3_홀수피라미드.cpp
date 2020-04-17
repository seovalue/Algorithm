#include<iostream>
using namespace std;
void init(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
}
int main(int argc, char** argv)
{
    init();
	int test_case;
	int T;
	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
		
        long long N, L, R;
        cin >> N;
         
 
        L = (N - 1) * (N - 1) + 1;
        R = N * N;
 
 
        cout << "#" << test_case << " " << 2 * L - 1 << " " << 2 * R  - 1<< "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
