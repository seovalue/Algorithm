#include <iostream>
#include <algorithm>
using namespace std;
bool compare(int& a, int& b){
    return a > b ? true : false;
}
int main(void){
    int arr[3];
    for(int i = 0; i < 3; i++){
        cin >> arr[i];
    }
    sort(arr, arr+3, compare);

    int n1 = arr[0] - arr[1];
    int n2 = arr[1] - arr[2];

    if(n1 > n2){
        cout << n1-1 << "\n";
    }else{
        cout << n2-1<<"\n";
    }

    return 0;
}
