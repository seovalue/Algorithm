//백준 9461번: https://www.acmicpc.net/problem/9461
// 미리 100까지의 값들을 저장해놓은 뒤 갖다 썼다.
// 규칙은 memo[i] = memo[i-1] + memo[i-5]

#include <iostream>
using namespace std;
int main(void){
    long long memo[101] = {0,1,1,1,2,2,};
    int n,t;
    for(int i = 6; i <= 100; i++){
        memo[i] = memo[i-1]+memo[i-5];
    }

    cin >> t;
    for(int i = 0; i< t; i++){
        cin >> n;
        cout << memo[n] << "\n";
    }
    return 0;
}
