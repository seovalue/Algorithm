#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
    int n;
    cin >> n;
    int dp[n], se[n];
    for(int i = 0; i < n; i++){
        cin >> dp[i];
        se[i] = dp[i];
    }

    int sum = 0, maxSum = dp[0];
    for(int i = 1; i < n; i++){
        dp[i] = max(dp[i],dp[i-1]+se[i]);
        if(dp[i] > maxSum) maxSum = dp[i];
    }

    cout << maxSum << "\n";
    return 0;
}
