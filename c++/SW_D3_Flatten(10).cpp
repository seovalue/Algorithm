#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool compare(int a, int b){
  return a > b ? true: false;
}
int main(void){
  int T = 10;
  int test_case;
  for(test_case = 1; test_case <= T; ++test_case)
	{
        int dump;
        cin >> dump;
        vector<int> asc, des;
        int num;
        for(int i = 0; i < 100; i++){
            cin >> num;
            asc.push_back(num);
			des.push_back(num);
        }
        while(dump > 0){
            sort(asc.begin(),asc.end()); //오름차순 정렬
            sort(des.begin(),des.end(),compare); //내림차순 정렬

            asc[0]++;
            des[0]--;

            dump--;
        }
        sort(asc.begin(),asc.end()); //오름차순 정렬
        sort(des.begin(),des.end(),compare); //내림차순 정렬
        cout << "#" << test_case << " " << des[0]-asc[0]<<"\n";
  }
  return 0;
}
