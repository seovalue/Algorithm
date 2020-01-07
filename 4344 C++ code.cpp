//백준 4344번 : https://www.acmicpc.net/problem/4344
/*
문제는 쉬운데 마지막에 소수점 셋째자리까지 출력하는 것이 문제였다. printf("%.3f",ratio) 이렇게 했더니 계속 나던 오류가, cout.precision(3); cout << fixed << ratio << "%\n";으로 하니 바로 정답으로 나왔다. printf와 scanf의 용법을 여전히 잘 모르고 있는 것 같다. C++ 에 관해서 더 공부를 해야할 것 같다.
*/

#include <iostream>
using namespace std;
int main(void)
{
    int C;
    cin >> C;
    for(int i = 0; i < C; i++)
    {
        int n;
        cin >> n;
        double sum = 0,  mean, ratio;
        int *stu = new int [n];
        if(n == 0) return 0;
        if(!stu) return 0;
        for(int i = 0; i < n; i++)
        {
            cin >> stu[i];
            sum += stu[i];
        }
        mean = sum / n;
        int cnt = 0;
        for(int i = 0; i < n; i++)
        {
            if(stu[i] > mean)
                cnt++;
        }
        ratio = ((double)cnt*100)/n;

        cout.precision(3); //소수점 셋째자리까지 출력
        cout << fixed << ratio << "%\n"; //fixed는 고정된 자릿수로 나타내겠다는 뜻
        delete[] stu;
    }
}
