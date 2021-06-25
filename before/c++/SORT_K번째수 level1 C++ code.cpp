#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> tmpanswer;
    int i,j,k;

    for(int n = 0; n < commands.size(); n++){
        i = commands[n][0];
        j = commands[n][1];
        k = commands[n][2];

        if(i == j){
            tmpanswer.push_back(array[i-1]);
        }else{
            for(int m = i-1; m < j ; m++){
                tmpanswer.push_back(array[m]);
            }
        }
        sort(tmpanswer.begin(),tmpanswer.end());
        answer.push_back(tmpanswer[k-1]);
        tmpanswer.clear();
    }
    return answer;
}
