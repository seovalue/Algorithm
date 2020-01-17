//백준 11654번: https://www.acmicpc.net/problem/11654
#include <iostream>
using namespace std;
int main(void){
    char asc; //캐릭터형으로 변수를 받은 뒤
    int iasc;
    cin >> asc;
    iasc = (int)asc; //정수형으로 바꾸면 자동으로 ASCII수로 변경된다.
    cout << iasc << "\n";

    return 0;
}
