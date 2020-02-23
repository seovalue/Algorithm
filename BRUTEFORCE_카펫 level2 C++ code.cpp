#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;
    int length = brown + red;
    for(int sero = 3; sero < length; sero++){
        if(length % sero == 0) //길이가 세로(높이)로 나누어떨어지면
        {
            int garo = length / sero;
            //위 아래 2행 제외, 양 옆 2열 제외한 값을 곱하면 red 내부값
            if((garo - 2) * (sero - 2) == red){
                answer.push_back(garo);
                answer.push_back(sero);
                break;
            }
        }
    }
    return answer;
}
