//백준 9095번: https://www.acmicpc.net/problem/9095
#include <iostream>
using namespace std;
int main(void){
    int test_case;
    cin >> test_case;
    int dp[11] = {1,};
    for(int i = 1; i < 11; i++){
        if(i-1 >= 0)
            dp[i] += dp[i-1];
        if(i-2 >= 0)
            dp[i] += dp[i-2];
        if(i-3 >= 0)
            dp[i] += dp[i-3];
    }

    for(int i = 0; i < test_case; i++){
        int n;
        cin >> n;
        cout << dp[n] << "\n";
    }
    return 0;
}
