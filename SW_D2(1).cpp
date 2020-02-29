#include<iostream>
#include <algorithm>
using namespace std;

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int test_case;
	int T,score;
	cin>>T;
    while(T > 0){
        int stu[1001] = {0,};
        int mod = 0, idx;
        cin >> test_case;
        for(int i = 0; i < 1000; i++){
            cin >> score;
            stu[score]++;
            if(stu[score] > mod){
                mod = stu[score];
                idx = score;
            }
            else if(stu[score] == mod){ //최빈값이 같은 경우 점수가 더 큰 것을 최빈값으로 채택
                if(score > idx){
                    mod = stu[score];
                    idx= score;
                }
            }
        }
        cout << "#" << test_case << " " << idx << "\n" ;
        T--;
    }
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
