//백준 1717번: https://www.acmicpc.net/problem/1717
/*
유니온 파인드를 이용해서 푸는 문제였다.
1. 부모배열이 모두 자기 자신을 가리키도록 세팅한다.
2. 입력이 0이면, 두개를 연결하고 부모를 합친다.
3. 입력이 1이면, 두개의 부모가 같은지 확인하고 같으면 yes, 틀리면 no를 출력한다.
*/

#include <iostream>
using namespace std;
int par[1000001];
int getParent(int par[],int x){ //부모를 리턴하는 함수
    if(par[x] == x) return x;
    return par[x] = getParent(par,par[x]);
}
void unionParent(int par[],int a,int b){ //부모를 합치는 함수
    a = getParent(par,a);
    b = getParent(par,b);
    if(a > b) par[a] = b;
    else par[b] = a;
}

bool findParent(int par[], int a, int b){ //부모가 같은지 확인하는 함수
    a = getParent(par, a);
    b = getParent(par, b);
    if(a==b) return true;
    else return false;
}
int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, m;
    cin >> n >> m;
    for(int i = 1; i<=n ; i++)
        par[i] = i;

    int a,b,c;
    for(int i = 1; i <= m; i++){
        cin >> a >> b >> c;
        if(a == 0){
            unionParent(par,b,c);
        }
        if(a == 1){
            if(findParent(par,b,c))
                cout << "YES\n";
            else
                cout << "NO\n";
        }
    }

    return 0;
}
