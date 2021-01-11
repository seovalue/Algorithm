#include <iostream>
using namespace std;
int main(void){
    int n,m;
    cin >> n >> m;
    cout << n*m - 1 << endl;
    /*
    세로가 N일 때 세로를 1로 만들기 위해서는 N-1번 잘라야함
    가로가 M일 때 가로를 1로 만들기 위해서는 M-1번 잘라야함
    -> 총 = N-1 + N(세로에서 잘린 조각의 개수) * (M - 1)
    -> N*M - 1
    */
    return 0;
}
