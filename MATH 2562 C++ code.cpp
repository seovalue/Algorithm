//백준 2562번: https://www.acmicpc.net/problem/2562

#include <iostream>
using namespace std;
int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int array[9];
    for(int i = 0; i < 9 ; i++)
        cin >> array[i];
    int idx, max = 0;
    for(int j = 0; j < 9; j++){
        if(array[j] > max)
        {
            max = array[j];
            idx = j;
        }
    }
    cout << max << "\n" << idx+1;
    return 0;
}
