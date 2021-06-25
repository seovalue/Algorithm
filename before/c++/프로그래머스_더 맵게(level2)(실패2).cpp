#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq;

    for(int i = 0; i < scoville.size(); i++)
        pq.push(scoville[i]);
    bool k = false;
    while(true){
        if(pq.size() == 1){
            k = true;
            break;
        }
        int n1 = pq.top();
        if(n1 >= K) return answer;
        pq.pop();
        int n2 = pq.top();
        pq.pop();

        int n3 = n1 + (n2 * 2);
        answer++;
        if(n3 >= K)
            break;
        pq.push(n3);
    }

    if(k && pq.top() < K) return -1;
    else return answer;
}
