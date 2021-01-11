//백준 2164번: https://www.acmicpc.net/problem/2164
#include <iostream>
#include <queue>
using namespace std;
int main(void){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n;
    cin >> n;
    queue<int> q;
    for(int i = 1; i <= n; i++){
        q.push(i);
    }
    while(1){
        if(q.size() == 1)
            break;
        q.pop(); //q의 제일 위 요소를 버린다.
        int front = q.front();
        q.pop();
        q.push(front);
    }
    cout << q.front() <<"\n";

    return 0;
}
