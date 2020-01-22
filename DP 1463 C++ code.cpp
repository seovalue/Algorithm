//백준 1463번 : https://www.acmicpc.net/problem/1463

#include <iostream>
using namespace std;
int memo[1000001];
int min(int x, int y){
    return x < y ? x : y; // x < y 이면 x를 리턴, 아니면 y를 리턴
}
int main(void){
    int n;
    scanf("%d",&n);
    memo[1] = 0;
    for(int i = 2; i <= n; i++){
        memo[i] = memo[i-1]+1; //예를 들어 3은 2+1 이므로 2의 memo값에 연산횟수 1회를 더한 것을 저장한다.
        if(i % 3 == 0)
            memo[i] = min(memo[i],memo[i/3]+1);
        if(i % 2 == 0)
            memo[i] = min(memo[i],memo[i/2]+1);
    }
    cout << memo[n] << "\n";
    return 0;
}
