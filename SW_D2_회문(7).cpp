#include<iostream>
#include<string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        string str;
        cin >> str;
        bool chk = true;
        for(int i = 0; i < str.size(); i++){
            int j = str.size()-i-1;
            if(str[i] != str[j])
                chk = false;
        }

        if(chk) cout << "#" << test_case << " 1\n";
        else cout << "#" << test_case << " 0\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
