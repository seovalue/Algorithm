#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;

    for(int i = 0; i < prices.size(); i++){
        int cnt = 0;
        for(int j = i+1; j < prices.size(); j++){
            if(prices[i] <= prices[j]){
                cnt++;
            }
            else{ //price[i] > price[j]인 경우 1초만큼만 증가시키고 for문을 중단
                cnt++;
                break;
            }
        }
        answer.push_back(cnt);
    }


    return answer;
}
