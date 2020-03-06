#include<iostream>

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
        int pascal[10][10]= {0};
        pascal[1][1] = 1;
        for(int i = 2; i <= n; i++){
            for(int j = 1; j <= i; j++){
                pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j];
            }
        }
        cout << "#" << test_case << "\n";
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= i; j++){
                cout << pascal[i][j] << " ";
            }
            cout << "\n";
        }
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
