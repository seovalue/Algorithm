#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq;

    for(int i = 0; i < scoville.size(); i++){
        pq.push(scoville[i]);
    }

    while(!pq.empty()){
        int n1 = pq.top();
        pq.pop();
        int n2 = pq.top();
        pq.pop();

        int n3 = n1 + ( n2 * 2);
        if(n3 >= K){
            answer++;
            break;
        }
        answer++;
        pq.push(n3);
    }
    return answer;
}
