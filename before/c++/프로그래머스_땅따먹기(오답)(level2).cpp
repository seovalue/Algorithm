#include <iostream>
#include <vector>
using namespace std;

int solution(vector<vector<int>> land)
{
    int answer = 0;
    int idx, beforeIdx;
    for(int i = 0; i < land.size(); i++){
        int max = 0;
        beforeIdx = idx;
        for(int j = 0; j < 4; j++){
          if(i == 0){
              if(land[i][j] > max ) {
                  beforeIdx = j;
                  idx = j;
                  max = land[i][j];
              }
          } else {
              if(land[i][j] > max){
                  if(beforeIdx != j){
                      max = land[i][j];
                      idx = j;
                  }
              }
          }
        }
        answer += max;
    }
    return answer;
}
