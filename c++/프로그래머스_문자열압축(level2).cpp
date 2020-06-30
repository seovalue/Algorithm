#include <string>
#include <vector>
#include <cmath>
#include <string.h>
using namespace std;

int solution(string s) {
    int answer = 1000;
    int n = s.length();
    int spl = 1;
    while(spl <= n){
      int size = ceil(double(n)/spl);
      int cntArr[n];
      memset(cntArr,0,sizeof(cntArr));
      string comp[size];
      int j = 0;
      for(int i = 0; i < n; i+=spl){
        if(i+spl > n){
            comp[j] = s.substr(i,n);
            continue;
        }
        comp[j] = s.substr(i,spl);
        j++;
      }
      int cnt, r = 0;
      while(r < size){
        cnt = 0;
        for(int j = r*comp[0].size() ; j < n; j+=spl){
            string tmp = "";
            for(int k = j; k < j+spl; k++){
              if(k > n) break;
              tmp += s[k];
            }
            if(comp[r] == tmp) cnt++;
            else break;
        }
        if(cnt == 1 || cnt == 0) cntArr[r] = 0+comp[r].size();
        else if(cnt >= 1 && cnt <= 9) cntArr[r] = 1+comp[r].size();
        else if(cnt >= 10 && cnt <= 99) cntArr[r] = 2+comp[r].size();
        else if(cnt >= 100 && cnt <= 999) cntArr[r] = 3+comp[r].size();
        else cntArr[r] = 4+comp[r].size();
        if(cnt == 0) r++;
        else r += cnt;
      }
      int sum = 0;
      for(int q = 0; q < n; q++){
        sum += cntArr[q];
      }
      if(sum == 0) sum = n;
      if(answer > sum){
        answer = sum;
      }
      spl++;
  }
  return answer;
}
