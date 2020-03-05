#include <iostream>
using namespace std;
int main(){
  int n;
  cin >> n;
  int tmp;
  for(int i = 1; i <= n; i++){
    bool chk = false;
    tmp = i;
    while(tmp > 0){
      int tmp2 = tmp % 10;
      if(tmp2 == 3 || tmp2 == 6 || tmp2 == 9){
        cout << '-';
        chk = true;
      }
      tmp /= 10;
    }
    if(chk == false)
      cout << i << " ";
    else
      cout << " ";
  }
  return 0;
}
