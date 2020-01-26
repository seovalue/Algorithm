//백준 10815번: https://www.acmicpc.net/problem/10815

#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n;
    cin >> n;
    int card[n];
    for(int i = 0; i < n; i++){
        cin >> card[i];
    }
    sort(card,card+n);
    int m;
    cin >> m;
    for(int i = 0; i < m; i++){
        int x;
        cin >> x;
        int start = 0, end = n-1;
        bool find = false;
        while(start <= end){
            int mid = (start+end) / 2;
            if(card[mid] == x)
            {
                find = true;
                break;
            }
            else if(card[mid] < x)
                start = mid + 1;
            else
                end = mid - 1;
        }
        if(find)
            cout << 1 << " ";
        else
            cout << 0 << " ";
    }
    return 0;
}
