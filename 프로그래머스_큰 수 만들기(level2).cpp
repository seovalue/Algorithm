#include <string>
#include <vector>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    int size = number.size() - k; //답의 길이

    int st = 0;
    for(int i = 0; i < size; i++){ //답의 길이만큼 반복
      char maxNum = number[st];
      int maxIdx = st;
      for(int j = st ; j <= i+k; j++){
         //j는 start 인덱스부터, i+k까지
         //i부터 k개까지만 답의 범위 안에 들어갈 수 있으므로
         // ex) 4글자 중 2글자를 제외한 경우에는 j = 0; j <= 2 이다. j=3인 경우를 택하면 다음 수를 택할 수 없기 때문
        if(maxNum < number[j]){
          maxNum = number[j];
          maxIdx = j;
        }
      }
      st = maxIdx + 1;
      answer += maxNum;
    }
    return answer;
}
