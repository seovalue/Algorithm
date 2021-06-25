#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(0); cin.tie(0);
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n,m;
        cin >> n >> m;
        int snack[n]; //과자의 무게를 저장하는 배열
        for(int i = 0; i < n; i++)
        {
            cin >> snack[i];  //과자 무게 저장
        }
        int max = -1;
        for(int i = 0; i < n; i++)
        {
            int sum = 0;
            if(snack[i] > m) continue; //m보다 과자의 무게가 크다면 넘어감
            for(int j = i+1; j < n; j++) //m보다 과자의 무게가 작을 때
            {
                sum = snack[i]+snack[j];
                if(sum <= m && sum > max)
                    max = sum;
            }
        }
        cout << '#' << test_case <<" "<<max << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
