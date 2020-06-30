//백준 1260번 : https://www.acmicpc.net/problem/1260

/*
DFS와 BFS
DFS는 깊이우선탐색으로 자식노드를 먼저 탐색한 후 형제노드를 탐색한다.

BFS는 너비우선탐색으로 형제노드를 먼저 탐색한 후 자식노드를 탐색한다.



문제를 해결하기 위해 주어진 map은 인접행렬로 나타낼 수 있다.

인접행렬은, i와 j의 인덱스를 바꾸어도 값이 변하지 않는 행렬로 map을 나타낼 때 주로 사용할 수 있는데,

예를 들어 주어진 데이터가 1-2 1-3 2-1 인 경우,

0 0 0 0

0 0 1 1

0 1 0 0

0 1 0 0 와 같이 나타낼 수 있다.

이 문제는 DFS와 BFS를 비교할 수 있는 문제였기 때문에 주어진 데이터를 이용해 인접행렬을 만들고 방문했다는 표시인 bool행렬 visit[MAX_SIZE]를 만들어 DFS에서는 방문한 노드인 경우에는 true, 아닌 경우에는 false를 BFS에서는 그 반대를 사용하여 나타내었다.
*/

#include <iostream>
#include <queue>
#define MAX_SIZE 1001 //MAX_SIZE는 N이 1부터 1000까지 였기 때문에 마지막 인덱스에 접근할 수 있도록 하기 위해 1001까지로 정의했다.
using namespace std;

int N,M,V;
int map[MAX_SIZE][MAX_SIZE];
bool visit[MAX_SIZE];
void dfs(int v)
{
    cout << v << ' ';
    visit[v] = true; //방문한 노드를 true로
    for(int i = 1; i <= N; i++) //N만큼의 for문을 돌렸을 때,
    {
        if(visit[i] == true || map[v][i] == 0) //이미 방문한 노드이거나 값이 0인 경우 (연결되지 않은 경우)이면
            continue; //아래 코드를 실행하지 않고 건너뜀.
        dfs(i); //재귀로 dfs 실행
    }
}
void bfs(int v)
{
    queue<int> q; //노드를 담을 q를 선언
    q.push(v); //q에 첫번째 노드를 push
    visit[v] = false; //방문했다는 의미로 false
    while(!q.empty()) //q가 비어있지 않은 동안
    {
        v = q.front(); //v를 q의 가장 첫번째 요소로
        cout << q.front() << ' '; //v를 출력
        q.pop(); //q의 가장 첫번째 요소를 삭제
        for(int i = 1; i <= N; i++)
        {
            if(visit[i] == false || map[v][i] == 0) //이미 방문했거나 연결되어있지 않은 경우
                continue; //아래 코드를 실행하지않고 건너뜀.
            q.push(i); //q에 i를 넣고,
            visit[i] = false; //방문했다는 의미로 false
        }
    }
}
int main(void)
{
    cin.tie(0); cout.tie(0);
    cin >> N >> M >> V;
    int x,y;
    for(int i = 0; i < M; i++)
    {
        cin >> x >> y;
        map[x][y] = map[y][x] = 1; //길이 있다는 의미로 인접행렬에서 1의 값을 줌.
    }
    dfs(V);
    cout << "\n";
    bfs(V);
    return 0;
}
