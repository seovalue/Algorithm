#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n,k, answer = 0;
        cin >> n >> k;
        int mat[15][15] = {0};
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> mat[i][j];
            }
        }
        int g_visit[15][15] = {0};
        int s_visit[15][15] = {0};
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(mat[i][j] == 1){
                    int g_cnt = 0;
                    for(int x = j; x < n; x++){
                        if(mat[i][x] == 0) break;
                        if(mat[i][x] == 1 && g_visit[i][x] == 0){
                            g_cnt++;
                            g_visit[i][x] = 1;
                        }
                    }
                    if(g_cnt == k) answer++;
                }
                if(mat[j][i] == 1){
                    int s_cnt = 0;
                    for(int x = j; x < n; x++){
                        if(mat[x][i] == 0) break;
                        if(mat[x][i] == 1 && s_visit[x][i] == 0){
                            s_cnt++;
                            s_visit[x][i] = 1;
                        }
                    }
                    if(s_cnt == k) answer++;
                }
            }
        }

        cout << "#" << test_case << " " << answer << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
