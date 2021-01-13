#include <algorithm>
#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int n;
        cin >> n;
        int arr[n];
        for(int i = 0; i < n; i++)
            cin >> arr[i];
        sort(arr,arr+n);

        cout << "#" << test_case << " ";
        for(int i = 0; i < n; i++){
            cout << arr[i] << " ";
        }cout << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
