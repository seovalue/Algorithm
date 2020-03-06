#include <iostream>
#include <algorithm>
using namespace std;
int main(void){
    int x, y, w, h;
    cin >> x >> y >> w >> h;

    int step = min(w-x, x);
    step = min(step,min(h-y,y));
    cout << step << "\n";

    return 0;
}
