#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
    int days[13] = {0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int month1, month2, day1, day2;
        cin >> month1 >> day1 >> month2 >> day2;

        int daySum = 0;

        if(month1 == month2)
            daySum += day2 - day1 + 1;
        else{
            for(int i = month1 + 1; i < month2 ; i++){
            	daySum += days[i];
        	}
        	daySum += (days[month1]-day1) +day2 + 1;
        }

        cout << "#" << test_case << " " << daySum << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
