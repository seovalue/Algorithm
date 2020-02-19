#include <string>
#include <vector>
using namespace std;

int solution(string dartResult) {
    int answer = 0;
    vector<int> vec;
    string number ="";
    int inumber = 0;

    for(int i = 0; i < dartResult.size(); i++){
        if(dartResult[i] >= '0' && dartResult[i] <= '9'){
            number += dartResult[i];
            continue;
        }
        if(dartResult[i] == 'S'){
            inumber = stoi(number);
            vec.push_back(inumber);
            number = "";
        }
        if(dartResult[i] == 'D'){
            inumber = stoi(number);
            vec.push_back(inumber * inumber);
            number = "";
        }
        if(dartResult[i] == 'T'){
            inumber = stoi(number);
            vec.push_back(inumber*inumber*inumber);
            number = "";
        }
        if(dartResult[i] == '#'){
            inumber = -1 * vec.back();
            vec.pop_back();
            vec.push_back(inumber);
        }
        if(dartResult[i] == '*'){
            inumber = 2 * vec.back();
            vec.pop_back();
            int tmpNumber = 2 * vec.back();
            vec.pop_back();
            vec.push_back(tmpNumber);
            vec.push_back(inumber);
        }
    }
    for(int i = 0; i < vec.size(); i++){
        answer += vec[i];
    }
    return answer;
}
