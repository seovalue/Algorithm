#include<iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int participant[2000][2000]; //참가자들의 점수 배열

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int test_case;
	int Test;
	cin >> Test;
	int N, T, P;
    int temp;

	for (test_case = 1; test_case <= Test; ++test_case)
	{
		cin >> N >> T >> P;
        int score[2000] = {0,}; //점수 배열을 0으로 초기화
		int count[2000] = {0,};  //맞춘 개수
		int totalScore[2000] = {0,};
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < T; ++j) {
                cin >> participant[i][j];
				if (participant[i][j] == 0)
					score[j]++;
				else
					count[i]++;
			}
		}
		for (int i = 0; i < T; ++i) {
			totalScore[P - 1] += participant[P - 1][i] * score[i];
		}
		int cnt = 1;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < T; j++) {
				if (i != P - 1)	totalScore[i] += participant[i][j] * score[j];
			}
			if (totalScore[i] > totalScore[P - 1]) cnt++;
			else if (totalScore[i] == totalScore[P - 1] && count[i] > count[P - 1]) cnt++;
			else if (totalScore[i] == totalScore[P - 1] && count[i] == count[P - 1] && i < P - 1) cnt++;
		}
		cout << "#" << test_case << " " << totalScore[P - 1] << " " << cnt << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
