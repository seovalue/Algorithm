//백준 10828번 : https://www.acmicpc.net/problem/10828

#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    stack<int> Stack;
    string command;
    int n;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> command;
        if(command == "push")
        {
            int x;
            cin >> x;
            Stack.push(x);
        }
        if(command == "top")
        {
            if(Stack.empty())
                cout << "-1\n";
            else
            {
                cout << Stack.top() << "\n";
            }
        }
        if(command == "size")
            cout << Stack.size() << "\n";
        if(command == "empty")
        {
            if(Stack.empty())
                cout << "1\n";
            else
                cout << "0\n";
        }
        if(command == "pop")
        {
            if(Stack.empty())
                cout << "-1\n";
            else
            {
                cout << Stack.top() << "\n";
                Stack.pop();
            }
        }
    }

    return 0;
}
