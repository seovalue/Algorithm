#include <string>
#include <vector>
#include <bitset>
using namespace std;
string Bit(int n, int num){
    string str = "";
    for (int i = n-1; i >= 0; i--)
        str += to_string(num >> i & 1 ? 1 : 0);
    return str;
}

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    string line1, line2;
    for(int i = 0; i < n; i++){
        line1 = Bit(n,arr1[i]);
        line2 = Bit(n,arr2[i]);
        string tmp = "";
        for(int j = 0; j < line1.size(); j++){
            if(line1[j] == '0'){
                if(line2[j] == '1') tmp+="#";
                if(line2[j] == '0') tmp+=" ";
            }
            else if(line1[j] == '1') tmp+="#";
        }
        answer.push_back(tmp);
    }
    return answer;
}
