//n/2 만큼만 합할 수 있음!!!!
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    for(int i = 1; i <= n/2+1; i++){
        int sum = 0;
        for(int j = i; j <= n/2+1; j++){
            sum += j;

            if(sum == n){
                answer++;
            }else if( sum > n ) break;
        }
    }
    return answer;
}
