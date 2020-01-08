//백준 1904번: https://www.acmicpc.net/problem/1904
// n == 2일 때 2라는 조건을 준 뒤 n>=3 이상일 때부터
// Tile(n) = Tile(n-1)+Tile(n-2) 를 이용하여 DP로 구현하였다.

#include <iostream>
using namespace std;
int memo[1000001];
int Tile(int n){
    if(n == 0) return 0;
    if(n == 1) return 1;
    if(n == 2) return 2;
    if(memo[n] != 0) return memo[n];
    return memo[n] = (Tile(n-1)+Tile(n-2)) % 15746;
}
int main(void){
    int n;
    cin >> n;
    cout << Tile(n) << "\n";
    return 0;
}
