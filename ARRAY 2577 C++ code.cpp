//백준 2577번: https://www.acmicpc.net/problem/2577

#include <iostream>
using namespace std;
int main(void){
    int a, b, c;
    int arr[10] = {0};
    cin >> a >> b >> c;
    int mul = a*b*c;

    while(mul != 0){
        arr[mul%10] += 1;
        mul /= 10;
    }
    for(int i = 0; i < 10; i++){
        cout << arr[i] << "\n";
    }
    return 0;
}
