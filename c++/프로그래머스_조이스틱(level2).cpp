#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    string tmp(name.length(),'A'); //A로 차있는 문자열 생성
    int i = 0;
    while(true){
        tmp[i] = name[i]; //tmp에 name을 복사
        name[i] - 'A' > 'Z'+1-name[i] ? answer+='Z'+1-name[i]:answer += name[i]-'A';
        // 'A'방향으로 이동하는 것과, 'Z'방향으로 이동하는 것 중 더 짧은 곳으로 이동, answer에 더함.
        if(tmp == name) break; //name과 tmp가 같으면 중단

        for(int j = 1; j < name.size(); j++){
            if(name[(i+j)%name.length()] != tmp[(i+j)%name.length()]){
              //오른쪽으로 이동하는 것
              // 주어진 문자열 name의 길이만큼 인덱스를 반복시키기 위해서 name.length()로 나눈 나머지값으로 인덱싱
              // j만큼 이동한 뒤, name.length()로 나누어줌.
              // name과 tmp의 오른쪽 이동 후 값이 다르면
                i = (i+j)%name.length(); //다음번 i의 인덱스를 그만큼 이동
                answer += j;
                break;
            } else if(name[(i+name.length()-j)%name.length()] != tmp[(i+name.length()-j)%name.length()]){
              //왼쪽으로 이동하는 것
                i = (i+name.length()-j)%name.length();
                answer += j;
                break;
            }
        }
    }

    return answer;
}
