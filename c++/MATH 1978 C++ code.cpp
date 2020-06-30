//백준 1978번: https://www.acmicpc.net/problem/1978

#include <iostream>
using namespace std;
bool isPrime(int n){
    if(n == 1) return false;
    if(n == 2) return true;
    for(int i = 2; i < n; i++){
        if(n % i == 0)
            return false;
    }
    return true;
}
int main(void){
    int n,m,cnt = 0;
    cin >> n;
    for(int i = 0; i< n; i++){
        cin >> m;
        if(isPrime(m))
            cnt++;
    }
    cout << cnt << "\n";
    return 0;
}
