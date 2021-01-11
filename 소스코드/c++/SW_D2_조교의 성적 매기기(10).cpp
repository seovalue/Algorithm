#include<iostream>
#include <string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int n, k;
        cin >> n >> k;
        double grade[n];
        for(int i = 0; i < n; i++){
            double mid, fin, hom;
            cin >> mid >> fin >> hom;
            grade[i] = mid * 0.35 + fin * 0.45 + hom * 0.2;
        }

        double std = grade[k-1];
        int cnt = 1;
        for(int i = 0; i < n; i++){
            if(grade[i] > std) cnt++;
        }

        int i = 0;
        string g[10] = {"A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"};
        while(true){
            if(cnt > (n/10)*i && cnt <= (n/10)*(i+1)){
                cout << "#" << test_case << " " << g[i] << "\n";
                break;
            }
            i++;
        }


	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
