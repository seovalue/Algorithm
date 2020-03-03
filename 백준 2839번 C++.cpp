#include <iostream>
#define LARGE 5
#define SMALL 3
using namespace std;
int solution(int& n){
    if ( n < SMALL) return -1;
    int div = n / LARGE;
    while(div >= 0){
        int tmp = n - div * LARGE;
        if(tmp % SMALL == 0)
            return div + tmp/SMALL;
        div--;
    }
    return -1;
}
int main(){
    int N;
    cin >> N;

    int result = solution(N);
    cout << result;

    return 0;
}
