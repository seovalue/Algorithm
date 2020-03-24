//for문은 증감이 먼저 일어난 뒤 조건을 확인함.
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(),people.end());
    int i = 0, j;
    for(j = people.size()-1; j > i; j--){
        if(people[i] + people[j] <= limit){
            answer++;
            i++;
        } else {
            answer++;
        }
    }

    if(j == i){
      answer++;
    }

    return answer;
}
