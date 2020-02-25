#include<string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    vector<int> garo;
    int sum = 0;
    if(s[0] == ')') return false;
    else{
        for(int i = 0; i < s.size();i++){
            if(s[i] == '(')
                garo.push_back(1);
            else
                garo.push_back(-1);
        }
        for(int i = 0; i < garo.size(); i++){
            sum += garo[i];
            if(sum < 0)
                return false;
        }
    }
    if(sum == 0) return true;
    if(sum > 0) return false;
}
