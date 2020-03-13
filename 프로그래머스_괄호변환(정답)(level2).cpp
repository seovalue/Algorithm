#include <string>
#include <vector>
#include <stack>
using namespace std;
stack<char> st;
bool checkGaro(string garo){
    while(!st.empty()) st.pop();
    if(garo[0] == ')') return false;
    for(int i = 0; i < garo.size(); i++){
        if(garo[i] == '(') st.push('(');
        else{ //')'
            if(!st.empty()){
                st.pop();
            } else {
                return false;
            }
        }
    }
    return true;
}
string func(string w){
    if(w == "") return w;
    string u,v;
    int left = 0, right = 0;
    for(int i = 0; i < w.size(); i++){
        if(w[i] == '(') left++;
        else right++;
        if(left == right){
            u = w.substr(0,i+1);
            v = w.substr(i+1);
            break;
        }
    }

    if(checkGaro(u)) return u+func(v);
    else{
        string answer = "(" + func(v) + ")";
        u = u.substr(1,u.size()-2);
        for(int j = 0; j < u.size(); j++){
            if(u[j] == '(') answer += ")";
            else answer += "(";
        }
        return answer;
    }
}
string solution(string p) {
    return func(p);
}
