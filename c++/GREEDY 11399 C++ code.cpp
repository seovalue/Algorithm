//백준 11399번: https://www.acmicpc.net/problem/11399

#include <iostream>
#include <algorithm>
using namespace std;
int man[1000];
int main(void){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> man[i];
    }
    sort(man,man+n);
    int sum = 0, total = 0;
    for(int i = 0; i<n; i++){
        sum += man[i];
        total += sum;
    }
    cout << total << "\n";
    return 0;
}
