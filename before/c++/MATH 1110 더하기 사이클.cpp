#include <iostream>
using namespace std;
int n;
int solution(int a, int b, int cnt){
    cnt++;
    int tmp = b * 10 + ((a+b) % 10);
    if(tmp == n)
        return cnt;
    return solution(tmp / 10, tmp % 10,cnt);
}
int main(void){
    cin >> n;
    int cnt = 0;
    cout << solution(n/10, n%10, cnt) << "\n";
    return 0;
}
