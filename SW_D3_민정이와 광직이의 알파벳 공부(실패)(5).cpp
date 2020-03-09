#include<iostream>
#include<set>
#include<string>
#include<vector>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n; cin >> n;
        string str;
        set<char> alp;
        vector<string> pass;
        int set = 0;
        for(int i = 0; i < n; i++){
            cin >> str;
            int size = alp.size();
            for(int j = 0; j < str.size(); j++){
                alp.insert(str[j]);
            }
            if(size == alp.size()) //모든 단어가 중복이어서 추가되지 않았다면
            {
                for(int j = 0; j < str.size(); j++){
                    pass.push_back(str);
                }
            }
            if(alp.size() == 26){
                set++;
                alp.clear();
            }
        }
        string ps;
        if(pass.size() > 0){
            for(int i = 0; i < pass.size(); i++){
                ps = pass[i];
                for(int j = 0; j < ps.size(); j++){
                    alp.insert(ps[j]);
                }
                if(alp.size() == 26){
                    set++;
                    alp.clear();
            	}
            }
        }

        printf("%s%d %d\n","#",test_case,set);

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
