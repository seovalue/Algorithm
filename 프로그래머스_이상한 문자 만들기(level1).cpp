#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool flag = true;
    for(int i = 0; i < s.size(); i++){
        if(s.at(i) == ' '){
            answer += ' ';
            flag = true; //flag 초기화
        }
        else{
            if(flag){
                flag = false;
                answer += toupper(s[i]);
                continue;
            }
            if(!flag){
                flag = true;
                answer += tolower(s[i]);
                continue;
            }
        }
    }
    return answer;
}
