#include <string>
#include <vector>
#include <sstream>
#include <map>
using namespace std;
vector<string> solution(vector<string> record) {
	vector<string> answer;
    vector<vector<string>> cmd(record.size(),vector<string>(3));
    //record.size() x 3으로 초기화
    map<string,string> info;

	for (int i = 0; i < record.size(); i++) {
		istringstream iss(record[i]); //" "로 분리
		iss >> cmd[i][0] >> cmd[i][1] >> cmd[i][2]; //cmd, id ,nick
        if(cmd[i][0] == "Enter" || cmd[i][0] == "Change"){
            info[cmd[i][1]] = cmd[i][2];
            //info["id"] = "nickname"
        }
	}
	for (int i = 0; i < cmd.size(); i++) {
		if (cmd[i][0] == "Enter") {
			answer.push_back(info[cmd[i][1]] + "님이 들어왔습니다.");
		}
		else if (cmd[i][0] == "Leave") {
			answer.push_back(info[cmd[i][1]] + "님이 나갔습니다.");
		}
	}
	return answer;
}
