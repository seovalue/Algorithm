#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    map<string,int> m;

    //key는 의상의 종류, value는 종류에 해당하는 옷의 수
    for(int i = 0; i < clothes.size(); i++){
        int value = m.find(clothes[i][1])->second;
        if(value == m.end()->second) m.insert(make_pair(clothes[i][1],1));
        else
            m[clothes[i][1]] = value + 1;
    }

    //조합의 수
    int comb = 1;
    for(auto i = m.begin(); i != m.end(); i++){
        comb *= i->second+1; //0의 경우도 세어줌
    }
    return comb - 1; //0의 경우를 빼줌
}
