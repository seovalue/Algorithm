#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int arr[30] = {0,};
    for(int i = 0; i < reserve.size(); i++){
        arr[reserve[i]-1] += 1;
    }
    for(int i = 0; i < lost.size(); i++){
        arr[lost[i]-1] += -1;
    }

    // 예제 #1 의 경우 arr = [1 -1 1 -1 1]
    for(int i = 0; i < n; i++){
        if(arr[i] == -1){
            if(i == n-1){
                if(arr[i-1] == 1) answer++;
            } else {
                if(arr[i-1] == 1){
                    answer++;
                    arr[i-1] = 0;
                    continue;
                }
                if(arr[i+1] == 1){
                    answer++;
                    arr[i+1] = 0;
                    continue;
                }
            }
        } else {
            answer++;
        }
    }

    return answer;
}
