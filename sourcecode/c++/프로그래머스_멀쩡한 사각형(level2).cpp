#include <iostream>
using namespace std;

// - w, h는 1억 이하의 수 ( 억 = 10^8 )
// 억 * 억 = 10 ^ 16 이므로 int에 담을 수 없다.
// long long 은 +- 9 * (10^16) 만큼 담을 수 있음 !!
//
// gcd는 int로 받고, answer을 계산할 때 w * h 는 int의 범위를 벗어나므로
// long long으로 타입을 변경해서 계산해준다.
//
// w * h 의 사이즈를 가진 사각형은 대각선을 지나는 gcd개 만큼의 블럭을 가지고,
// 그 블럭은 w / gcd, h/ gcd (가로 , 세로)의 크기를 가진다.
// 그 블럭 안에서 대각선 아래에 놓인 블럭은 총 w / gcd + h / gcd - 1 개 이다.

int get_gcd(int w, int h){
    if(h == 0) return w;
    else
        return get_gcd(h, w%h);
}
long long solution(int w,int h)
{
	long long answer;
    int gcd = get_gcd(w,h);
    answer = (long long)w * (long long)h - ( w/gcd + h/gcd - 1) * gcd;

	return answer;
}
