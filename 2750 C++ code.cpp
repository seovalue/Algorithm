//백준 2750번: https://www.acmicpc.net/problem/2750

//삽입정렬을 이용해서 풀었는데, 삽입정렬은 데이터를 순차적으로 정렬하면서 현재 값을 정렬되어 있는 값들과 비교해 적합한 위치로 삽입하는 방식이다. 반복문의 시작을 배열의 두번째부터 진행해 순서대로 앞의 것과 비교하면서 정렬해나가는 방식이다.

#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    int n, dummy;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    for(int i = 0; i < n; i++)
    {
        dummy = arr[i];
        int j = i;

        while(arr[j-1] > dummy && j > 0)
        {
            arr[j] = arr[j-1];
            j--;
        }
        arr[j] = dummy;
    }

    for(int i = 0; i < n; i++)
        cout << arr[i] << "\n";
    return 0;
}
