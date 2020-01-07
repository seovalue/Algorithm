//백준 1712번: https://www.acmicpc.net/problem/1712
/*
고정비용 : a, 가변비용 : b, 판매비용 : c 라고 했을 때, 손익분기점을 x라고 하면 간단히 생각해보았을 때 총비용 < 총판매금액 을 만족해야하므로 먼저, 총 비용 = 총 판매금액 이 되는 x 값을 계산해보면
a+b*x = c*x <=> (b-c)*x = -a <=> x = a/(c-b) 이므로 x = a / (c-b) 가 되어야함을 알 수 있다. 여기서 손익분기점이 되기 위해서는 우변이 1이라도 더 커야하므로 손익분기점 x 는 a/(c-b)+1임을 알 수 있다.
손익분기점이 발생하지 않는 경우는 c-b <=0 인 경우에는 만족하지 않음을 알 수 있다.
*/
#include <iostream>
using namespace std;
int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int a, b, c;
    cin >> a >> b >> c;

    int par = c - b;
    if(par <= 0) cout << -1 << "\n";
    else
        cout << a/par + 1;
    return 0;
}
