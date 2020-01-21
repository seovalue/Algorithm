//백준 5585번: https://www.acmicpc.net/problem/5585
#include <iostream>
using namespace std;
int main(void){
    int m, cnt = 0;
    cin >> m;
    m = 1000 - m;
    while(m > 0){
        if(m >= 500){
            cnt++;
            m -= 500;
            continue;
        }
        if(m >= 100){
            cnt++;
            m -= 100;
            continue;
        }
        if(m >= 50){
            cnt++;
            m-= 50;
            continue;
        }
        if(m>=10){
            cnt++;
            m-= 10;
            continue;
        }
        if(m>=5){
            cnt++;
            m-=5;
            continue;
        }
        if(m>=1){
            cnt++;
            m-=1;
            continue;
        }
    }
    cout << cnt << "\n";
    return 0;
}
