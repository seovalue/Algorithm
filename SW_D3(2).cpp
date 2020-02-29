#include<iostream>
#include <algorithm>
using namespace std;

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int T = 10, test_case = 0;
    int size;
    int arr[1001];
    int adj[4];
    while( T > 0 ){
        int answer = 0;
        cin >> size;
        for(int i = 0; i < size; i++) cin >> arr[i]; //arr에 주어진 값을 모두 집어넣음.

        // 0 0 ~~~ 으로 시작하므로 2번째 인덱스부터 시작, ~~ 0 0으로 끝나므로 size - 2까지
        for(int i = 2; i < size - 2; i++){
            if(arr[i] > arr[i-1] && arr[i] > arr[i-2] && arr[i] > arr[i+1] && arr[i] > arr[i+2]){
                adj[0] = arr[i-2];
                adj[1] = arr[i-1];
                adj[2] = arr[i+1];
                adj[3] = arr[i+2];

            	sort(adj, adj+4);
            	answer += arr[i] - adj[3];
            }
        }
        cout << "#" << ++test_case << " " << answer <<"\n";
        T--;
    }
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
