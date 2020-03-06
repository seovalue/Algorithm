#include <iostream>
using namespace std;
int main(void){
    int n, tmp;
    cin >> n;
    int sum = 0, max = 0;
    for(int i = 0; i < n; i++){
        cin >> tmp;
        if(tmp > 0) sum += tmp;
        if(max < sum) max = sum;
        if(tmp < 0 && i != 0) sum = 0;
    }
    cout << max << "\n";
    return 0;
}
