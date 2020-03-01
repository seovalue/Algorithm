#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    map<char,int> m;
    for(int i = 0; i < skill.size(); i++){
        m.insert(make_pair(skill[i],i+1));
    }
    for(int i = 0; i < skill_trees.size(); i++){
        int cnt = 1;
        bool find = true;
        for(int j = 0; j < skill_trees[i].size(); j++){
            if(m.find(skill_trees[i][j])->second != m.end()->second){
                if(m.find(skill_trees[i][j])->second != cnt){
                    find = false;
                    break;
                }
                else
                    cnt++;
            }
        }
        if(find) answer++;
    }


    return answer;
}
