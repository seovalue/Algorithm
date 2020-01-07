//백준 2798번 : https://www.acmicpc.net/problem/2798
/*
주어진 카드를 반복문을 돌려 모든 경우의 수를 다 합해본 뒤 M보다 작거나 같은 경우일 때, SUM 이라는 변수를 두어 M - ( CARD[i] + CARD[j] + CARD[k]) < M - SUM 인 경우에 SUM에 세 카드의 합을 저장하는 방법을 통해 모든 경우의 수에서 가장 M가 가까운 합을 찾도록 한다.
*/

#include <iostream>
using namespace std;
int main(void)
{
    cin.tie(NULL); cout.tie(NULL);
    int n,m, sum = 0;
    cin >> n >> m;
    int card[n];
    for(int i = 0; i < n; i++)
        cin >> card[i];
    for(int i = 0; i < n-2; i++)
    {
        for(int j = i+1; j < n-1; j++)
        {
            for(int k = j+1; k < n; k++)
            {
                if(card[i]+card[j]+card[k] <= m)
                {
                    if(m-(card[i]+card[j]+card[k]) < m - sum)
                       sum = card[i] + card[j] + card[k];
                }
            }
        }
    }

    cout << sum;
    return 0;
}
