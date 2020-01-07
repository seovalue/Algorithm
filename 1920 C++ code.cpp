//백준 1920번 : https://www.acmicpc.net/problem/1920

#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    cin.tie(NULL);

    int n;
    cin >> n;
    int A[n+1];
    for(int i = 0; i < n; i++)
        cin >> A[i];
    sort(A,A+n);

    int m;
    cin >> m;
    int search[m+1];
    for(int i = 0; i < m; i++)
    {
        cin >> search[i];
        bool found = false;
        int start = 0, end = n, middle;
        while(start <= end)
        {
            middle = (start + end) / 2;
            if(search[i] == A[middle])
            {
                found = true;
                break;
            }
            else if(search[i] > A[middle])
                start = middle+1;
            else
                end = middle - 1;
        }
        if(found) cout << "1\n";
        else cout << "0\n";
    }
    return 0;
}
