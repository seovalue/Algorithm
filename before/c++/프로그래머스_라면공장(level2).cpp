#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    int i = 0;
    priority_queue<int, vector<int>> pq;

    for(int day = 0; day < k; ++day){
        if(dates[i] == day){
            pq.push(supplies[i]);
            if(i != supplies.size()) i++;
        }
        if(stock == 0){
            stock += pq.top();
            answer++;
            pq.pop();
        }
        stock--;
    }
    return answer;
}
