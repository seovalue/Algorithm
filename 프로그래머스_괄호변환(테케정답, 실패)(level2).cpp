#include <string>
#include <vector>
#include <stack>
using namespace std;
string u;
string v;
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
void split(string p){
  int sum = 0;
  u = ""; v = "";
  u += p[0];
  if(p[0] == '('){
    sum += 1;
  } else {
    sum += -1;
  }
  for(int i = 1; i < p.size(); i++){
    if(sum == 0){
      v += p[i];
      continue;
    }
    else {
      if(p[i] == ')'){
      u+=p[i];
      sum += -1;
      }
      else{
        u+=p[i];
        sum += 1;
      }
    }
  }
}
string solution(string p) {
    string answer = "";
    string tmp1 = "", tmp2 = "";
    if(checkGaro(p) || p.size() == 0) return p;
    else{
        bool flag = false;
        v = p;
        while(true){
          if(v.size() == 0){
              if(flag){
                  for(int i = 1; i < tmp1.size() - 1; i++){
                      tmp2 += tmp1[i];
                  }
                  for(int j = 0; j < tmp2.size(); j++){
                      if(tmp2[j] == ')') answer += ')';
                      else answer += '(';
                  }
                  answer += ")";
              }
              break;
          }
          split(v); //u,v로 분리
          if(checkGaro(u)){
              answer += u;
          }
          else {
              tmp1 += u;
              answer += "(";
              flag = true;
          }
        }
    }
    return answer;
}
