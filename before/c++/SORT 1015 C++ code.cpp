//백준 1015번: https://www.acmicpc.net/problem/1015

#include <iostream>
using namespace std;
int main(void){
    int arr[51], P[51];
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    int minIndex = 0;
    for(int i = 0; i < n; i++){
        int min = 1001; //배열에 해당하는 수는 1000보다 작거나 같은 자연수라고 했기 때문
        for(int j = 0; j < n; j++){
            if(arr[j] < min){
                min = arr[j];
                minIndex = j;
            }
        }
        P[minIndex] = i;
        arr[minIndex] = 1001;
    }
    for(int i = 0; i < n; i++)
        cout << P[i] << " ";
    return 0;
}
