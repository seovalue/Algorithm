#include <string>
#include <vector>
using namespace std;
int solution(int n) {
    int dp[n];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;

    for(int i = 3; i <= n; i++){
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007;
    }
    /*
    int answer = 0;
    for(int i = 3; i <= n; i++){
        dp[i] = dp[i-1] + dp[i-2];
    }
    answer = dp[n] % 1000000007;
    -> 에러
    */

    return dp[n];
}
