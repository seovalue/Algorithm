//백준 2751번: https://www.acmicpc.net/problem/2751
#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr,arr+n);
    for(int i = 0; i < n; i++){
        cout << arr[i] << "\n";
    }
    return 0;
}
