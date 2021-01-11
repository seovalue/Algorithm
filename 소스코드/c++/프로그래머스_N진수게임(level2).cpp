#include <string>
#include <vector>

using namespace std;

string notation(int n, int x){ //x라는 수를 n진법으로 바꿔주는 함수
    string answer = "";
    char ch[16] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    while(x > 0){ //몫이 0이 될 때까지
        answer = ch[x%n] + answer; //answer의 앞에 추가함
        x /= n;
    }
    return answer;
}

string solution(int n, int t, int m, int p) {
    string answer = "";
    string note = "0";
    for(int i = 0; i < t * m; i++){
        note += notation(n,i); //총 t*m개의 숫자를 n진법으로 변환해놓음
    }
    int i = p-1;
    while(true){
        if(answer.size() == t) break;
        answer += note[i];
        i += m;
    }
    return answer;
}
