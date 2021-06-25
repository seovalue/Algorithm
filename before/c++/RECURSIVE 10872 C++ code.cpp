//백준 10872번 : https://www.acmicpc.net/problem/10872

/*
구현 아이디어

1! = 1

0! = 1

이라는 Base Case를 바탕으로 재귀함수로 구현하였다.
*/

#include <iostream>
using namespace std;
int factorial(int n)
{
    if(n == 1 || n == 0)
        return 1;
    return n * factorial(n-1);
}
int main(void)
{
    int n;
    scanf("%d",&n);
    printf("%d",factorial(n));
    return 0;
}
