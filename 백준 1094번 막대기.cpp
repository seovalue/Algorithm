#include <iostream>
using namespace std;

int main(void){
    int x;
    cin >> x;
    int cnt = 1, min = 64, sum = 64;
    while( sum > x){
        min = min / 2;
        if(sum - min >= x){
            sum -= min;
        }else{
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}
