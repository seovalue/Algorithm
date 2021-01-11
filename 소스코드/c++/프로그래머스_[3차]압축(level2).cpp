#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    vector<string> dic = {"0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
"Q","R","S","T","U","V","W","X","Y","Z" };
    vector<string>::iterator it;
    for(int i = 0; i < msg.size(); i++){
        bool flag = true;
        string w = "";
        while(flag){
            int idx;
            w += msg[i];
            it = find(dic.begin(), dic.end(), w);
            if(it != dic.end()){
                idx = it - dic.begin();
                i++;
            }
            else{
                answer.push_back(idx);
                dic.push_back(w);
                i--;
                flag = false;
            }
        }
    }
    return answer;
}
