#include<iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char** argv)
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int test_case;
	int T;
	cin>>T;
    string str;
    getline(cin,str);
	for(test_case = 1; test_case <= T; ++test_case)
	{
        string answer = "";
        getline(cin,str);
		bool space = false;
        answer += toupper(str[0]);
        for(int i = 0; i < str.length(); i++){
            if(space){
                answer += toupper(str[i]);
                space = false;
            }
            if(str[i] == ' ') space = true;
        }
        cout << "#" << test_case << " " << answer << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
