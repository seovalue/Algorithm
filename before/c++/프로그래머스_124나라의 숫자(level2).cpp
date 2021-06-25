#include <string>
#include <vector>

using namespace std;
vector<string> base = {"4","1","2"};
string solution(int n) {
    string answer = "";
    while(n != 0){
        answer.insert(0,base[n%3]);
        if(n % 3 == 0) n = n / 3 - 1; //3의 배수들은 3때문에 1씩 남음
        else n /= 3;
    }
    return answer;
}
