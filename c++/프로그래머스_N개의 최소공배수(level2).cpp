// gcd, lcm 구하는 방법 외워두기
#include <string>
#include <vector>

using namespace std;
int gcd(int a, int b){
	while(b!=0){
		int r = a%b;
		a= b;
		b= r;
	}
	return a;
}

int lcm(int a, int b){
    return a * b / gcd(a,b);
}

int solution(vector<int> arr) {
    int answer = lcm(arr[0],arr[1]);
    for(int i = 2; i < arr.size(); i++){
       answer =lcm(answer,arr[i]);
    }
    return answer;
}
