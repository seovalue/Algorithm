#include<iostream>
#include<vector>
using namespace std;
vector<vector<int>> snale;
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
int main(int argc, char** argv)
{
    int test_case;
    int T;
    cin>>T;
    for(test_case = 1; test_case <= T; ++test_case)
    {
        int n;  cin >> n;
        snale = vector <vector<int>>(n, vector<int>(n, 0)); //snale[n][n] 을 모두 0으로 초기화
        int cnt = 1, loc = 0; //cnt는 snale안에 넣을 변수, loc은 dx,dy로 위치 이동시킬 변수
        snale[0][0] = cnt; //snale[y][x]
        int x = 0, y = 0;
        while(true){
            if(x + dx[loc] >=0 && y + dy[loc] >=0 && x + dx[loc] < n && y + dy[loc] < n && !snale[y+dy[loc]][x+dx[loc]])
            {
                //x+dx[loc], y+dy[loc]이 존재하고, 0인 경우 (값이 초기화 되지 않은 경우)
                cnt++;
                x = x + dx[loc];
                y = y + dy[loc];
                snale[y][x] = cnt;
            }
            else{
                if(loc == 3)    loc =0;
                else    loc++;
            }
            if(cnt == n*n) break;
        }
        cout << "#" << test_case << "\n";
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cout << snale[i][j] << " ";
            }
            cout << "\n";
        }
    }
    return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
