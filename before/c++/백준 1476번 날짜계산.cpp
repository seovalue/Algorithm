#include <iostream>
using namespace std;
int main(void){
    int e,s,m;
    cin >> e >> s >> m;
    int i = 1;
    while(true){
        if((i-e) % 15 == 0 && (i-s) % 28 == 0 && (i-m) % 19 == 0)
            break;
        i++;
    }
    cout << i;
}
