//백준 10870번: https://www.acmicpc.net/problem/10870
//재귀함수를 이용한 피보나치 수열 구현

#include <iostream>
using namespace std;
int Fibo(int n){
    if(n == 0) return 0;
    if(n == 1 || n == 2) return 1;
    return Fibo(n-1)+Fibo(n-2);
}
int main(void)
{
    int n;
    cin >> n;
    cout << Fibo(n) <<"\n";
    return 0;
}
