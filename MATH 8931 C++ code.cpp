#include<iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv)
{
    int test_case;
    int T;
    cin>>T;
    for(test_case = 1; test_case <= T; ++test_case)
    {
        cout << "#" << test_case << " ";
        int k, n, sum = 0;
        vector<int> vec;
        cin >> k;
        for(int i = 0; i < k; i++)
        {
            cin >> n;
            if( n != 0)
                vec.push_back(n);
            else
                vec.pop_back();
        }

        while(!vec.empty())
        {
            int tmp = vec.back();
            sum += tmp;
            vec.pop_back();
        }
        cout << sum << "\n";
    }
    return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
