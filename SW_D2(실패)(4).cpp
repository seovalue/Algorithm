#include<iostream>
#include <string>
using namespace std;

int main(int argc, char** argv)
{
	int n;
    cin >> n;
    string ans = "";
    for(int i = 1; i <= n; i++)
        ans += to_string(i);

    for(int i = 0; i < ans.size(); i++){
        if(ans[i] == '3' || ans[i] == '6' || ans[i] == '9'){
            ans[i] = '-';
        }
    }
    string tmp = "";
    for(int i = 1; i <= ans.size(); i++){
        if(i>=10 && i < 189){
            tmp+= ans[i-1];
            tmp+= ans[i];
            cout << tmp << " ";
            tmp="";
            i += 1;
        }
        else if (i>=189 && i < 2889){ //191
            tmp += ans[i-1];
            tmp += ans[i];
            tmp += ans[i+1];
            cout << tmp << " ";
            tmp="";
            i += 2;
        }
        else if(i >= 2889){ //2892
            cout << "1000";
            break;
        }
        else{
            cout << ans[i-1] << " ";
        }
    }
    cout << "\n";
    return 0;
}
