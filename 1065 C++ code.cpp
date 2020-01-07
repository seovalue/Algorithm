//백준 1065번 : https://www.acmicpc.net/problem/1065

/*
한수의 개념이 등장하는데, 어떤 양의 정수 X의 자릿수가 등차수열을 이룬다면, 그 수를 한수라고 부른다.

예를 들자면 111은 공차가 0인 한수, 123은 공차가 1인 한수가 된다.

수를 입력받은 뒤, 그 수가 한수인지 확인하는 함수를 만들었다. 한자리수와 두자리수는 자기 자신이 한수가 되므로 자기 자신을 출력하도록 만들었고, 세자리 수부터는 최소 한수인 99를 더한 뒤 각 i마다 자릿수를 구하여 자릿수끼리의 차가 같으면 한수이므로 카운트를 증가시켜 카운트를 리턴하도록 만들었다.
*/

#include <iostream>
using namespace std;
int IsSequence(int n)
{
    int cnt = 0;
    if(n < 100)
        cnt = n;
    else
    {
        cnt = 99;
        for(int i = 100; i <= n; i++)
        {
            if(i == 1000)
                return cnt;
            int n1 = i % 10; //1의자리
            int n2 = i % 100 / 10; //십의자리
            int n3 = i / 100; //백의자리
            if((n3 - n2) == (n2 - n1))
                cnt++;
        }
    }
    return cnt;
}
int main(void)
{
    cin.tie(NULL);
    int n, answer;
    cin >> n;
    answer = IsSequence(n);
    cout << answer;
    return 0;
}
