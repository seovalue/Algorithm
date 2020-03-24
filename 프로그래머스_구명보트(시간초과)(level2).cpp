#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> people, int limit) {
    vector<int> boat;
    int i = 1, cnt = people.size()-1;
    boat.push_back(people[0]);
    while(cnt != 0){
        bool flag = false;
        for(int j = 0; j < boat.size(); j++){
            int sum = 0;
            sum = boat[j] + people[i];
            if(sum <= limit){
                boat[j] = sum;
                cnt--;
                flag = true;
                j = boat.size();
            }
        }
        if(!flag){
            boat.push_back(people[i]);
            cnt--;
        }
        i++;
    }
    return boat.size();
}
