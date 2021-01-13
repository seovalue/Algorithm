//백준 10809번: https://www.acmicpc.net/problem/10809
#include <iostream>
#include <string>
using namespace std;
int main(void){
    string alp;
    cin >> alp;

    int idx;
    for(char a = 'a'; a <='z'; a++){
        idx = alp.find(a);
        cout << idx << " ";
    }cout << "\n";
    return 0;
}
