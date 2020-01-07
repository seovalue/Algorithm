//백준 1427번: https://www.acmicpc.net/problem/1427

/*
처음 내가 생각한 방법은, string으로 받은 뒤 array에 수들을 나눈 뒤 (str = "1234"이면 array = [1|2|3|4]) 배열 내부에서 대소를 비교해서 swap 하는 방법을 생각했는데, 틀렸다고 해서 찾아보니 algorithm라이브러리를 그냥 사용하기만 하면 되는 문제였다. c++ 에서 기본적으로 주어지는 라이브러리에 무엇이 있는지 제대로 알아야할 필요가 있다고 느꼈다.
*/

#include <iostream>
#include <algorithm>
using namespace std;
int main(void)
{
    string n;
    cin >> n;
    sort(n.begin(), n.end(), greater<char>()); //greater<type>()을 쓰면 내림차순으로 정렬이 된다.
    cout << n;
}
