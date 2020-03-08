#include<iostream>
#include <string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int n; cin >> n;
        string ans= "";
        string alph;
        int x;
        cout << "#" << test_case << "\n";
        for(int i = 0; i < n; i++){
            cin >> alph >> x;
            for(int j = 0; j < x; j++)
            {
                if(ans.size() == 10){
                    cout << ans << "\n";
                    ans = "";
                }
                ans += alph;
            }
        }
        cout << ans << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
