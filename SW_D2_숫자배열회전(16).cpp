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
        int matrix[n][n];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> matrix[i][j]; //initialize matrix
            }
        }

        string ans[n][n];

        //90도
        string tmp = "";
        for(int i = 0; i < n; i++){
            for(int j = n-1; j >= 0; j--){
                tmp += to_string(matrix[j][i]);
            }
            ans[i][0] = tmp;
            tmp = "";
        }

        //180도
        for(int i = n-1; i >= 0; i--){
            for(int j = n-1; j >= 0; j--){
                tmp += to_string(matrix[i][j]);
            }
            ans[n-i-1][1] = tmp;
            tmp = "";
        }

        //270도
        for(int i = n-1; i >= 0; i--){
            for(int j = 0; j < n; j++){
                tmp += to_string(matrix[j][i]);
            }
            ans[n-i-1][2] = tmp;
            tmp ="";
        }

        cout << "#" << test_case << "\n";
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cout << ans[i][j] << " ";
            }
            cout << "\n";
        }

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
