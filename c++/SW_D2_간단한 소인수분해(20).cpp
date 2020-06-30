#include<iostream>
using namespace std;
int num[5] = {2,3,5,7,11};
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n; cin >> n;
        int cnt[5] = {0,};
        for(int i = 0; i < 5; i++){
            while(true){
                if(n%num[i] == 0){
                    cnt[i]++;
                    n /= num[i];
                }
                else break;
            }
        }
        cout << "#" << test_case << " ";
        for(int i = 0; i < 5; i++)
            cout << cnt[i] << " ";
        cout << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
