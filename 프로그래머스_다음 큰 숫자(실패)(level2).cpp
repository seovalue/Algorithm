#include <string>
#include <vector>

using namespace std;
int count(int n){
    int cnt = 0;
    for(int i = n; i > 0; i--){
        if(n % 2 == 1) cnt++;
        n /= 2;
    }
    return cnt;
}
int solution(int n) {
    int cnt1 = count(n);
    while(true){
        n++;
        int cnt2 = count(n);
        if(cnt1 == cnt2) break;
    }
    return n;
}
