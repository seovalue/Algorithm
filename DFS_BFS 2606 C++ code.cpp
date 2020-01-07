//백준 2606번: https://www.acmicpc.net/problem/2606
/*
연결되어있는 노드만 확인하면 되는 문제이기 때문에 dfs라고 부를 수 있는지
정확히 잘 모르겠다.. Union Find로 풀어도 된다고 하는데 어쨌든 연결이 되어있는
노드에 대해서 cnt를 증가시킨 뒤 cnt를 출력하도록 구현하였다.
*/

#include <iostream>
using namespace std;
int com,cnt;
int net[101][101];
int chk[101];
void NumOfVirus(int start)
{
    chk[start] = 1;
    for(int i = 1; i <= com; i++)
    {
        if(!chk[i] && net[start][i] == 1)
        {
            cnt++;
            NumOfVirus(i);
        }
    }
}
int main(void)
{
    int line,a,b;
    cin >> com >> line;
    for(int i = 0; i < line; i++)
    {
        cin >> a >> b;
        net[a][b]=net[b][a]=1;
    }
    NumOfVirus(1);
    cout << cnt << "\n";
    return 0;
}
