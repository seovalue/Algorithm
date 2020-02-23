#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> baseball) {
    int answer = 0;

    int strike = 0;
    int ball = 0;
    string ans = "";
    string num = "";

    // 각 자리 같은 수 안됨, 0 안됨
    for(int i = 123; i <= 987; i++){
        ans = to_string(i);

        if(ans[0] == ans[1] || ans[1] == ans[2] || ans[2] == ans[0])
            continue;
        if(ans[0] == '0' || ans[1] == '0' || ans[2] == '0')
            continue;

        bool test = true;
        for(int j = 0; j < baseball.size(); j++){
            strike = 0;
            ball = 0;
            num = to_string(baseball[j][0]);
            for(int a = 0; a < 3; a++){
                for( int b= 0; b < 3; b++){
                    if(a == b && ans[a] == num[b]){
                        strike++;
                        continue;
                    }
                    if(a != b && ans[a] == num[b]){
                        ball++;
                        continue;
                    }
                }
            }
            if(strike != baseball[j][1] || ball != baseball[j][2]){
                test = false;
                break;
            }
        }
        if(test){
            answer++;
        }
    }

    return answer;
}
