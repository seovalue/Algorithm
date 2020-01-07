// 백준 10845번 C++ 풀이(https://www.acmicpc.net/problem/10845)
// C++에 있는 STL library 중 queue를 이용하여 구현하였다.

#include <iostream>
#include <queue>
#include <string>
using namespace std;
queue<int> q;
int main(void){
    int n;
    cin >> n;
    string str;
    while(n--)
    {
        cin >> str;
        if(str == "push"){
            int num;
            cin >> num;
            q.push(num);
        }
        else if(str == "front")
        {
            if(!q.empty())
                cout << q.front() << "\n";
            else
                cout << "-1\n";
        }
        else if(str == "back")
        {
             if(!q.empty())
                 cout << q.back() << "\n";
            else
                cout << "-1\n";
        }
        else if(str == "size")
        {
            cout << q.size() << "\n";
        }
        else if(str == "empty")
        {
            if(q.empty())
                cout << "1\n";
            else
                cout << "0\n";
        }
        else if(str == "pop")
        {
            if(!q.empty())
            {
                cout << q.front() << "\n";
                q.pop();
            }
            else
                cout << "-1\n";
        }
    }
    return 0;
}
