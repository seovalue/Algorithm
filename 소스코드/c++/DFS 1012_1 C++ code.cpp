//백준 1012번: https://www.acmicpc.net/problem/1012
//dfs이용, visit 사용하지 않고 푼 방법.

#include <iostream>
using namespace std;
int d[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};
void dfs(int map[52][52],int i, int j){
    if(map[i][j] == 0)
        return;
    map[i][j] = 0;
    for(int k = 0; k < 4; k++){
        dfs(map,i+d[k][0],j+d[k][1]);
    }
}
int main(void){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T;
    cin >> T;
    while(T > 0){
        int map[52][52] = {0,};
        int M,N,K;
        cin >> M >> N >> K;
        for(int i = 0; i < K; i++){
            int x,y;
            cin >> x >> y;
            map[y+1][x+1] = 1;
        }
        int cnt = 0;
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= M; j++){
                if(map[i][j] == 1){
                    cnt++;
                    dfs(map,i,j);
                }
            }
        }
        cout << cnt << "\n";
        T--;
    }
    return 0;
}
