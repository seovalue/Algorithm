//백준 2581번: https://www.acmicpc.net/problem/2581

#include <iostream>
using namespace std;
bool isPrime(int n){
    if(n==1) return false;
    if(n==2) return true;
    for(int i = 2; i <= n/2; i++){
        if(n % i == 0)
            return false;
    }
    return true;
}
int main(void){
    int n,m, min = 10000, sum = 0;
    cin >> m;
    cin >> n;
    for(int i = m; i <=n; i++){
        if(isPrime(i)){
            sum += i;
            if(min > i)
                min = i;
        }
    }
    if(sum == 0){
        cout << "-1\n";
    }else
    {
        cout << sum << "\n" << min << "\n";
    }
    return 0;
}
