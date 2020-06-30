#include <string>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;
    stack<int> st;

    bool found = false;
    for(int j = heights.size()-1; j >= 0; j--){
        for(int i = j-1; i >= 0; i--){
            if(heights.at(i) > heights.at(j)){
                st.push(i+1); //i는 0부터 시작
                found = true;
                break;
            }
        }
        if(!found){
            st.push(0);
        }
        found = false;
    }

    while(!st.empty()){
        answer.push_back(st.top());
        st.pop();
    }
    return answer;
}
