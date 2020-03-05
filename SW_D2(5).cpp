#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int arr[15][15];
        int n, m;
        cin >> n >> m;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> arr[i][j];
            }
        }

        int max = 0;
				// i,j는 기준 시작점으로 생각
        for(int i = 0; i <= n-m; i++){ // i를 0부터 n-m만큼 반복
            for(int j = 0; j <= n-m; j++){ //j를 0부터 n-m만큼 반복
                int total = 0;
                // i,j를 고정시키고 (시작점을 고정시킴) m*m 만큼 이동하면서 값을 더함!
                for(int y = i; y < i+m; y++){ //y좌표를 i에서 i+m만큼 (i를 기준으로 0부터 m만큼)
                    for(int x = j; x < j+m; x++){
                        total += arr[y][x];
                    }
                }
                if(max < total) max = total;
            }
        }

        cout << "#" << test_case << " " << max << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
