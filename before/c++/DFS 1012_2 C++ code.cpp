//백준 1012번: https://www.acmicpc.net/problem/1012
//dfs이용, visit 사용하고 푼 방법.
//visit을 사용할 때는 memset으로 할당해주고, visit에 접근하기 위해서
// isInside 라는 함수를 이용해서 좌표가 범위 내에 있는지 확인해야한다.

#include <iostream>
#include <cstring>
using namespace std;
int d[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};
bool visit[52][52];
int map[52][52];
int M,N;
bool isInside(int y, int x){
    return (0<=y && y<N) && (0<=x && x<M);
}
void dfs(int map[52][52],int i, int j){
    if(visit[i][j]) return;
    visit[i][j] = true;
    for(int k = 0; k < 4; k++){
        int dy = i+d[k][0];
        int dx = j+d[k][1];
        if(isInside(dy,dx))
        {
            if(map[dy][dx]==1 && visit[dy][dx]==false)
                dfs(map,dy,dx);
        }
    }
}
int main(void){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T;
    cin >> T;

    while(T > 0){
        memset(visit,false,sizeof(visit));
        memset(map,0,sizeof(map));
        int K;
        cin >> M >> N >> K;
        for(int i = 0; i < K; i++){
            int x,y;
            cin >> x >> y;
            map[y][x] = 1;
        }
        int cnt = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(map[i][j] == 1 && visit[i][j] == false){
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
