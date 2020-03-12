#include<iostream>
#include <string>
#include <algorithm>
using namespace std;
bool compare(int a, int b){
    return a > b ? true: false;
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int og[7] = {0};
        int as[7] = {0};
        int v[7] = {0};
        int n; string str;
        cin >> str >> n;
        for(int i = 0; i < str.size(); i++){
            og[i] = as[i] = str[i] - '0';
        }
        sort(as,as+7,compare);

        if(str.size() == 1){
            cout << "#" << test_case << " " << og[0] << "\n";
        }

        int target = 0;
        bool isSwap, isHere = false;
        for(int i = 0; i < str.size() - 1; i++){
            if(n == 0) break;
            if(v[i]) continue;
            if(og[i] == as[i]) continue;
            // i 고정, j 변함
            isSwap = false;
            for(int j = i+1; j < str.size(); j++){
                isHere = true;
                if(og[j] == as[i]){
                    target = j;
                    if(og[i] == as[j]){
                        swap(og[i],og[j]);
                        isSwap = true;
                        v[j] = true;
                        n--;
                        break;
                    }
                }
            }
            if(!isSwap){
                swap(og[i], og[target]);
                n--;
            }
        }

        if(n){
            if(isHere){
                swap(og[str.size()-1],og[str.size()-2]);
            }
        }

        cout << "#" << test_case << " ";
        for(int i = 0; i < str.size(); i++){
            cout << og[i];
        } cout << "\n";
	}

	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
