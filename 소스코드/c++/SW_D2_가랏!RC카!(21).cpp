#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n, cmd, a;
        cin >> n;
        int v[n];
        for(int i = 0; i < n; i++){
            cin >> cmd;
            if(cmd == 0){
                if(i == 0) //초기속도
                    v[i] = 0;
                else
                    v[i] = v[i-1];
            }
            if(cmd == 1){
                cin >> a;
                if( i == 0) v[i] = a;
                else if(v[i - 1] >= 0) v[i] = v[i-1] + a;
            }
            if(cmd == 2){
                cin >> a;
                if(i==0 || v[i-1] == 0) v[i] = 0;
                else if(v[i-1] > 0){
                    if(v[i-1]-a < 0) v[i] = 0;
                    else v[i] = v[i-1]-a;
                }
            }
        }

        int sum = 0;
        for(int i = 0; i < n; i++){
            sum += v[i];
        }

        cout << "#" << test_case << " " << sum << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
