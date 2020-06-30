#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string number, int k) {
    string answer = "0";
    k = number.size() - k;
    string tmp = "";
    for(int i = 0 ; i < number.size(); i++){
      tmp += number[i];
      for(int j = i+1; j < number.size(); j++){
          if(j+k-2 >= number.size()) j = number.size();
          tmp += number.substr(j,k-1);
          if(stoi(answer) < stoi(tmp)){
            answer = tmp;
          }
          tmp = number[i];
      }
      tmp = "";
    }
    return answer;
}

int main(void){
  cout << solution("4177252841",4);

  return 0;
}
