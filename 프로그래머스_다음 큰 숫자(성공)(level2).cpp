#include <string>
#include <vector>
#include <bitset>
using namespace std;

int solution(int n) {
	int cnt = bitset<20>(n).count();
    //max가 1,000,000이므로 2^20-1 까지 가능한 20으로 할당
	while (true){
        n++;
        if(bitset<20>(n).count() == cnt) break;
    }

	return n;
}
