#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool compare(int a, int b){
    return a > b ? true : false;
}

int solution(vector<int> citations) {
    sort(citations.begin(), citations.end(),compare);
    for(int i = 0; i < citations.size(); i++){
        if(citations[i] < i+1)
            return i;
    }

    return citations.size();
}
