#include<iostream>
#include <cmath>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		double sum = 0;
       	int tmp, max = 0, min = 10001;
        for(int i = 0; i < 10; i++){
            cin >> tmp;
            sum += tmp;
            if(tmp > max) max = tmp;
            if(tmp < min) min = tmp;
        }
        sum -= (max + min);
        double avg = sum / 8;
        cout << "#" << test_case << " " << round(avg) << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
