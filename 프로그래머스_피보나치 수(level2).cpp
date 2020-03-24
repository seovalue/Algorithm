#include <string>
#include <vector>
using namespace std;
int Fibo[100001] = {0,1,};
int solution(int n) {
    for(int i = 2; i <= 100000; i++){
        Fibo[i] = (Fibo[i-1]+Fibo[i-2]) % 1234567;
    }
    return Fibo[n];
}
