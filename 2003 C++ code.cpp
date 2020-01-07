//백준 2003번: https://www.acmicpc.net/problem/2003
/*
두개의 포인터를 움직여가면서 합과 같아지는 경우 CNT를 증가시키고, 아닌 경우는 포인터를 움직이는 것인데 자연수인 경우에만 적용가능하므로 이 문제에서도 적용할 수 있었다.
*/

#include <iostream>
#include <vector>
using namespace std;
int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m;
    cin >> n >> m;
    vector<int> a(n);
    for(int i = 0; i < n; i++)
        cin >> a[i];

    int le = 0, ri = 0; //left와 right 포인터 선언 및 같은자리
    int sum = a[0];
    int cnt = 0; //카운트
    while(ri < n && le <= ri)
    {
        if(sum == m) //sum이 m과 같아지면
        {
            cnt++; //카운트를 1 증가시키고
            ri++; //right 포인터를 1 증가시킨다
            sum += a[ri];
        }
        else if(sum < m) //sum이 m보다 작으면
        {
            ri++; //right포인터를 1 증가시키고
            if(ri >= n) break; //만약 ri가 n보다 크거나 같으면 중단
            sum += a[ri];
        }
        else //sum이 m보다 크면
        {
            sum -= a[le];
            le++; //left 포인터를 1 증가시키고
            if(le > ri) //le가 ri를 넘었으면
            {
                ri = le; //ri와 le를 같은 자리로 초기화
                if(le < n)
                    sum = a[ri]; //합 초기화
            }
        }
    }

    cout << cnt;
    return 0;
}
