#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;
bool isPrime(int i, string numbers){
    vector<bool> visit(numbers.length());
    bool test = false;
    while(i != 0){
        test = false;
        int tmp = i % 10;
        for(int j = 0; j < numbers.length(); j++){
            if(tmp == numbers[j] - '0' && visit[j] == false){
                // tmp == numbers 숫자 변환과 같고, 방문한 적이 없다면
                visit[j] = true;
                test = true;
                break;
            }
        }
        // 한자리 수라도 포함하지 않는다면 false 리턴
        if(test == false)
            return false;
        // 포함된 경우 i가 0이 될때까지 반복
        i /= 10;
    }
    return true;
}

int solution(string numbers) {
    int answer = 0;
    sort(numbers.begin(), numbers.end(), greater<int>()); //내림차순 정렬
    vector<bool> era(stoi(numbers)+1);
    for(int i = 2; i <= stoi(numbers); i++){
        if(era[i] == false && isPrime(i,numbers))
            answer++;
        if(era[i] == false){
            for(int j = i; j <= stoi(numbers); j += i){
                era[j] = true;
            }
        }
    }
    return answer;
}
