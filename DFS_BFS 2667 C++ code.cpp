//백준 2667번: https://www.acmicpc.net/problem/2667

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n, cnt; //개수, 같은 단지에 속할 가구를 세는 변수
int house[25][25];
bool visit[25][25];
int d[4][2] = {{-1,0},{1,0},{0,1},{0,-1}}; //주변 확인용
vector<int> vtown;
bool isInside(int a, int b){ //영역안에 포함되어있는지를 확인
    return (a < n && a >= 0) && (b < n && b >= 0);
}
void dfs(int a, int b){
    cnt++;
    visit[a][b] = true;
    for(int i = 0; i < 4; i++){
        int dy = a + d[i][0];
        int dx = b + d[i][1];
        if(isInside(dy,dx) && visit[dy][dx] == false &&
          house[dy][dx] == 1)
            dfs(dy,dx);
    }
}
int main(void){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n;
    string temp;
    for(int i = 0; i < n; i++){
        cin >> temp; //string 변수로 읽어들임
        for(int j = 0; j < n; j++){
            house[i][j] = temp[j]-'0'; //ASCII코드로 변환해서 int로 저장
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(house[i][j] == 1 && visit[i][j] == false)
            {
                cnt = 0;
                dfs(i,j);
                vtown.push_back(cnt);
            }
        }
    }

    sort(vtown.begin(), vtown.end());
    cout << vtown.size() << "\n";
    for(int i = 0; i < vtown.size(); i++){
        cout << vtown[i] << "\n";
    }

    return 0;
}
