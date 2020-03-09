#include <iostream>
#include <cmath>
using namespace std;
int main(void){
    int n; cin >> n;
    int arr[11] = {0};
    int set = 0;
    if(n == 0) arr[0]++;
    while(n > 0){
        int idx = n % 10;
        if(n%10 == 9) idx = 6;
        arr[idx]++;
        n /= 10;
    }
    set = round(arr[6]/2);
    for(int i = 0; i < 11; i++){
        if(i == 6) continue;
        if(set < arr[i]) set = arr[i];
    }
    cout << set << "\n";
    return 0;
}
