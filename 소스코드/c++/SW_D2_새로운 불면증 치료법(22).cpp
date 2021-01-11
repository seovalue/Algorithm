#include<iostream>
#include <set>
#include <string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n, ntimes;
        cin >> n;
        ntimes = n;
        string sn = to_string(n);
        set<char> num;
        num.clear();
        int cnt = 1;
        while(true){
        	string sn = to_string(ntimes);
            cnt++;
            for(int i = 0; i < sn.size(); i++){
                num.insert(sn[i]);
            }
            if(num.size() == 10) break;
            ntimes = n * cnt;
        }
        printf("%s%d %d\n","#",test_case, ntimes);
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
