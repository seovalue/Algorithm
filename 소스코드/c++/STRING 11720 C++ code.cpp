//백준 11720번: https://acmicpc.net/problem/11720
//ASCII 코드를 이용하여 '0'을 뺐을 때 실제 10진수와 같은 수가 된다는 것을 이용했다.

#include <iostream>
using namespace std;
int main(void){
    int n, sum = 0, tmp;
    cin >> n;
    char c;
    while(n--)
    {
        cin >> c;
        sum += c - '0';
    }
    cout << sum;
    return 0;
}
