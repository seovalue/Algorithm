#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int change[8][2] = {{50000,0}, {10000,0}, {5000,0}, {1000,0}, {500,0}, {100,0}, {50,0}, {10,0}};
        int money;
        cin >> money;
        while(money>0){
            if(money / 50000 > 0){
                change[0][1] += money/50000;
                money %= 50000;
            }
            if(money / 10000 > 0){
                change[1][1] += money / 10000;
                money %= 10000;
            }
            if(money / 5000 > 0){
                change[2][1] += money / 10000;
                money %= 5000;
            }
            if(money / 1000 > 0){
                change[3][1] += money / 1000;
                money %= 1000;
            }
            if(money / 500 > 0){
                change[4][1] += money / 500;
                money %= 500;
            }
            if(money / 100 > 0){
                change[5][1] += money / 100;
                money %= 100;
            }
            if(money / 50 > 0){
                change[6][1] += money / 50;
                money %= 50;
            }
            if(money / 10 > 0){
                change[7][1] += money / 10;
                money %= 10;
            }
        }

        cout << "#" << test_case << " ";
        for(int i = 0; i < 8; i++){
            cout << change[i][1] << " ";
        }cout << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
