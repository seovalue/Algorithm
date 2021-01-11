#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool compare(string &a, string &b){
// a = 1 b = 10인 경우, a+b(110), b+a(101) 중 더 큰 순으로 정렬
// 위 경우 false이므로, 10 1 순으로 정렬
    return a+b < b+a ? true:false;
}
string solution(vector<int> numbers) {
    string answer = "";
    vector<string> svec;

    for(int i = 0; i < numbers.size(); i++){
        svec.push_back(to_string(numbers.at(i)));
    }

    sort(svec.begin(), svec.end(),compare);

    while(!svec.empty()){
        answer += svec.back();
        svec.pop_back();
    }

    if(answer[0] == '0') return "0";

    return answer;
}
