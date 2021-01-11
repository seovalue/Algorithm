#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
    int n; cin >> n;
    int arr[10] = {0};
    int set = 0;
    if(n == 0) arr[0]++;
    while(n > 0){
        arr[n % 10]++;
        n /= 10;
    }
    for(int i = 0; i < 10; i++){
        if( i != 6 && i != 9){
            set = max(set,arr[i]);
        }
    }
    cout << max(set,(arr[6]+arr[9]+1)/2) << "\n";
    return 0;
}
