//백준 2748번: https://www.acmicpc.net/problem/2748
// 입력받는 정수가 90까지로 늘어났기 때문에 long long int를 이용하고,
// memoization을 이용하여 DP로 구현하였다.

#include <iostream>
using namespace std;
long long int memo[91];
long long int Fibo(int n){
    if(n==0) return 0;
    if(n==1 || n==2) return 1;
    if(memo[n] != 0) return memo[n];
    return memo[n] = Fibo(n-1)+Fibo(n-2);
}
int main(void){
    int n;
    cin >> n;
    cout << Fibo(n) << "\n";
    return 0;
}
