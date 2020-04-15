#include<iostream>
using namespace std;

void init(){
	ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
}

int main(int argc, char** argv)
{
    init();
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int N,B,E,cnt = 0;
        cin >> N >> B >> E;
        for(int i = 0; i < N; i++){
            int tmp;
            cin >> tmp;
            int n = 1;
            bool flag = false;
            while(true){
                if(flag) break;
                if(n * tmp > B + E) break;
                if(n * tmp >= B - E && n * tmp <= B + E){
                    cnt++;
                    flag = true;
                }
                n++;
            }
        }
        cout << "#" << test_case << " " << cnt << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
