#include<iostream>
#include <algorithm>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
    int sum, max;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int n, m;
        cin >> n >> m;
        bool flag = false;
        if(n > m){
            swap(n,m);
            flag= true;
        }
        int aj[n], bj[m];

        if(flag)
        {
            for(int i = 0; i < m; i++)
            	cin >> bj[i];
            for(int i = 0; i < n; i++)
            	cin >> aj[i];
        }
        else{
            for(int i = 0; i < n; i++)
            	cin >> aj[i];
            for(int i = 0; i < m; i++)
            	cin >> bj[i];
        }

        int arr[n];
       	max = 0;
        for(int i = 0; i < m - n + 1; i++){
            int q = 0;
            for(int j = i; j <= i + n - 1; j++){
                arr[q] = bj[j];
                q++;
            }

            sum = 0;
            for(int k = 0; k < n; k++){
                sum += (arr[k] * aj[k]);
            }
            if(max < sum) max = sum;

        }

        cout << "#" << test_case << " " << max << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
