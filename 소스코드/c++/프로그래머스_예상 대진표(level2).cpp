#include <iostream>
using namespace std;

int solution(int n, int a, int b)
{
    int answer = 0;
    while(true){
        answer++;
        int achk = 0, bchk = 0;
        for(int i = 1; i <= n; i++){
            achk++;
            if(2 * i >= a) {
                a = i;
                break;
            }
        }
        for(int i = 1; i <= n; i++){
            bchk++;
            if(2 * i >= b) {
                b = i;
                break;
            }
        }
        if(achk == bchk) break;
        n /= 2;
    }

    return answer;
}
