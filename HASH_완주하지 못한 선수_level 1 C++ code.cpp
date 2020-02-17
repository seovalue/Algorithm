#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map<string,int> result;
    for(int i = 0; i < completion.size();i++){ //completion을 map에 넣는 과정
        int chk = result.find(completion[i])->second;
        if(chk == result.end()->second) //아무것도 없거나 동명이인이 존재하지 않음
            result.insert(make_pair(completion[i],1));
        else //동명이인 존재
            result[completion[i]] = chk+1; //한명을 더해줌
    }

    for(int i = 0; i < participant.size(); i++){
        int chk = result.find(participant[i])->second;
        if(chk == 0 || chk == result.end()->second)
            //part의 이름이 comp에 존재하지 않는 경우
            return participant[i];
        else
            result[participant[i]] = --chk;
    }
}
