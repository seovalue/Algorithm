//백준 2231번: https://www.acmicpc.net/problem/2231
/*
브루트 포스 알고리즘을 이용해서 푸는 방법. 브루트 포스 알고리즘이라 하면 별건 없고 모든 경우를 다 테스트해본다는 뜻이다. 반복문을 돌려 0부터 n까지 모든 경우를 계산한 뒤 주어진 N과 같아진 경우 return한다.
*/

#include <iostream>
using namespace std;
int Constructor(int n){
    int i = n;
    while(n!=0)
    {
        int j = n%10;
        i += j;
        n /= 10;
    }
    return i;
}
int Result(int n){
    for(int i = 0; i < n; i++){
        if(Constructor(i) == n)
            return i;
    }
    return 0;
}
int main(void){
    int n;
    scanf("%d",&n);
    printf("%d",Result(n));
    return 0;
}
