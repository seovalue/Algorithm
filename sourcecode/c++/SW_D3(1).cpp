#include<iostream>
#include<string>
using namespace std;
bool isUpper(char ch){
    if(ch >= 'A' && ch <= 'Z')
        return true;
    return false;
}

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false); cin.tie(false); cout.tie(false);
	int test_case;
	int T, slength;
    string answer, seokchan;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int result = 0;
		cin >> slength;
        cin >> answer;
        cin >> seokchan;
        for(int i = 0; i < slength; i++){
            if(isUpper(answer[i]) == 1 && isUpper(seokchan[i]) == 1){ //둘다 대문자인 경우
                if(answer[i] == seokchan[i]) result++;
            }
            else if(isUpper(answer[i]) == 0 && isUpper(seokchan[i]) == 0){ //둘다 소문자인 경우
                if(answer[i] == seokchan[i]) result++;
            }
        }
        cout << "#"<<test_case << " "<<result << "\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
