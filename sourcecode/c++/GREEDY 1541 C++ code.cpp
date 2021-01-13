//백준 1541번 : https://www.acmicpc.net/problem/1541

#include <iostream>
#include <string>
using namespace std;
int main(void){
    string str, tmp="";
    cin >> str;
    int sum = 0;
    bool minus = false;
    for(int i = 0; i <= str.size(); i++){
        if(str[i] == '+' || str[i] == '-' || str[i] == '\0'){
            if(minus) sum -= stoi(tmp);
            else
                sum += stoi(tmp);
            tmp = "";
            if(str[i] == '-')
                minus = true;
        }
        else
            tmp += str[i];
    }
    cout << sum << "\n";
    return 0;
}
