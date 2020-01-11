//SW Academy: Summation

#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
  int test_case;
	int T, n;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int max = 0, min = 1000000;
		    cout << "#" << test_case << " ";
        for(int i = 0; i < 10; i++)
        {
            cin >> n;
            int sum = 0;
            while(n!=0){
        	  sum += n % 10;
            n /= 10;
       		  }
            if(sum > max)	max = sum;
            if(sum < min)	min = sum;
        }
        cout << max << " " << min << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
