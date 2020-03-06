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
		int n;
        cin >> n;
        string arr[n];
        string line = "", saveLine ="";
        for(int i = 0; i < n; i++){
            line = "";
            for(int j = 0; j <= i; j++){
            	if(j == 0) line+="1";
                else if(j == i) line+="1";
                else{
                    line += saveLine[j-1]+saveLine[j] - '0';
                }
            }
            arr[i] = line;
            saveLine ="";
            saveLine += line;
		}
        cout << "#" << test_case << "\n";
        for(int i = 0; i < n; i++){
            cout << arr[i] << "\n";
        }
    }

	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
