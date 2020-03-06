#include <iostream>
using namespace std;
int main(void){
    int x, y, w, h;
    cin >> x >> y >> w >> h;
    if(w-x > h-y) cout << h-y << "\n";
    else cout << w-x << "\n";
    return 0;
}
