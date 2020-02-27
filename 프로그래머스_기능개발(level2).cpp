#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int day = 0;
    int func = 0;
    while(func != progresses.size()){
        int cnt = 0;
        day++;
        for(int i = func; i < progresses.size(); i++){
            if(progresses[func] + (speeds[func] * day) >= 100){
                cnt++;
                func++;
            }
        }
        if(cnt != 0)
            answer.push_back(cnt);
    }

    return answer;
}
