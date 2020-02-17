#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

bool solution(vector<string> phone_book) {
    map<string,int> m;
    int min = phone_book[0].length(); //0번째 string의 길이를 min으로 선언
    int max = 0;

    for(int i = 0; i < phone_book.size(); i++){ //해시맵에 각각 넣음
        if (min > phone_book[i].length()) min = phone_book[i].length();
        if (max < phone_book[i].length()) max = phone_book[i].length();
        m.insert(make_pair(phone_book[i],1));
    }

    for(int i = min; i <= max; i++){
        for(int j = 0; j < phone_book.size(); j++){
            if(phone_book[j].length() < i) continue;
            string sub = phone_book[j].substr(0,i);
            //0부터 i개의 substring을 구함
            if(sub.compare(phone_book[j]) == 0) continue; //같으면 넘어감
            if(m.find(sub)->second == 1) return false;
            // sub 해시값이 존재하면 return false
        }
    }
    return true;
}
