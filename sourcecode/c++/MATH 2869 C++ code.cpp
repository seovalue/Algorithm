//백준 2869번 https://www.acmicpc.net/problem/2869

#include <iostream>
using namespace std;
int main(void){
    int a,b,v,d;
    cin >> a >> b >> v;
    d = (v - b - 1) / (a - b) + 1;
    cout << d << "\n";
    return 0;
}
