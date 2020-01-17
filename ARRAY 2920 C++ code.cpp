//백준 2920번: https://www.acmicpc.net/problem/2920
#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
    int scale[8];
    int asc = 0, des = 0;
    for(int i = 0; i < 8; i++){
        cin >> scale[i];

        if(scale[i] == i+1)
            asc++;
        else if(scale[i] == 8-i)
            des++;
    }
    if(asc == 8)
        cout << "ascending\n";
    else if(des == 8)
        cout << "descending\n";
    else
        cout << "mixed\n";
    return 0;
}
