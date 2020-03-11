#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int N,M;
int dir[2] = {1,-1}; //상하좌우 탐색을 위한 dir
int bfs(int i, int j, vector<vector<int>>& picture, vector<vector<bool>>& visit){
    visit[i][j] = true;
    queue<pair<int,int>> q;
    q.push(make_pair(i,j));
    int color = picture[i][j];
    int area = 0;
    //주변 탐색
    while(!q.empty()){
        //color를 가진 area 하나 추가
        area++;
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        //같은 색을 가진 area 모두 방문
        for(int d = 0; d < 2; d++){
            if(x-dir[d] >= 0 && x - dir[d] < N && !visit[y][x-dir[d]] && color == picture[y][x-dir[d]]){
                q.push(make_pair(y,x-dir[d])); //탐색하다가 만나는 새로운 노드 q에 추가
                visit[y][x-dir[d]]=true;
            }
            if(y-dir[d] >= 0 && y- dir[d] < M && !visit[y-dir[d]][x] && color == picture[y-dir[d]][x]){
                q.push(make_pair(y-dir[d],x));
                visit[y-dir[d]][x]=true;
            }
        }
    }
    return area;
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    N = n; M = m;
    vector<vector<bool>> visit(m,vector<bool>(n,false));
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(picture[i][j] != 0 && !visit[i][j]){
                number_of_area++;
                int tmp = bfs(i,j,picture,visit);
                max_size_of_one_area = max_size_of_one_area > tmp ? max_size_of_one_area : tmp;
            }
        }
    }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
