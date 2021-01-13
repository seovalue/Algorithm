#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer, tmp;
    answer.push_back(0); //맨 처음은 0으로 시작함
    if(n == 1) return answer;
    for(int i = 2; i <= n; i++){
        tmp = answer; //tmp에 answer 대입
        answer.push_back(0); //0을 기준으로 0->1, 1->0 대칭 구조를 가짐
        for(int j = tmp.size() - 1; j >= 0; j--){
            if(tmp[j] == 0) answer.push_back(1);
            else answer.push_back(0);
        }
    }

    return answer;
}
