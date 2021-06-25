#include<iostream>
#include<string>
using namespace std;
int main(int argc, char** argv)
{
	int test_case;
    int T;
    cin >> T;
	for (test_case = 1; test_case <= T; ++test_case) {
        string n; cin >> n;
        if(n[2] >= '5'){
            if(n[1] == '9'){
                if(n[0] == '9'){
                    cout << "#" << test_case << " 1.0*10^" << n.size() << "\n";
                } else {
                    n[0]++;
                    n[1] = '0'; //그냥 0으로 하면 안됨. 
                    cout << "#" << test_case << " " << n[0] << "." << n[1] << "*10^" << n.size()-1 << "\n";
                }
            } else {
                n[1]++;
                cout << "#" << test_case << " " << n[0] << "." << n[1] << "*10^" << n.size()-1 << "\n";
            }
        } else {
            cout << "#" << test_case << " " << n[0] << "." << n[1] << "*10^" << n.size()-1 << "\n";
        }
	}
	return 0;
}
