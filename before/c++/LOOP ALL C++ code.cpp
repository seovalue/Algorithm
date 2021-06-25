//백준 사이트의 for 문 문제 전부에 대한 해답
#include <iostream>
using namespace std;
int main(void){
    int N;
    cin >> N;
    for(int i = 1; i <= 9; i++){
        cout << N << " * " << i << " = " << N*i << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    int T;
    cin >> T;
    while(T--){
        int a,b;
        cin >> a >> b;
        cout << a+b << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    int n;
    cin >> n;
    int sum = 0;
    for(int i = 1; i <= n; i++){
        sum += i;
    }
    cout << sum << "\n";
    return 0;
}

#include <iostream>
using namespace std;
int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while(T--){
        int a,b;
        cin >> a >> b;
        cout << a+b << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++)
        cout << i << "\n";
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;
    int cnt = n;
    while(1){
        if(cnt == 0)
            break;
        cout << n << "\n";
        n--;
        cnt--;
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    int T, test_case;
    cin >> T;
    for(test_case = 1; test_case <= T; ++test_case){
        int a,b;
        cin >> a >> b;
        cout << "Case #" << test_case <<": " << a+b << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    int T, test_case;
    cin >> T;
    for(test_case = 1; test_case <= T; ++test_case){
        int a,b;
        cin >> a >> b;
        cout << "Case #" << test_case <<": " << a << " + " <<b <<" = " << a+b << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < i+1; j++){
            cout << "*";
        }
        cout << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(j<n-i-1) cout <<" ";
            else cout << "*";
        }
        cout << "\n";
    }
    return 0;
}

#include <iostream>
using namespace std;
int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n, x;
    cin >> n >> x;
    int val;
    for(int i = 0; i < n; i++)
    {
        cin >> val;
        if(val < x)
            cout << val << " ";
    }
    return 0;
}
