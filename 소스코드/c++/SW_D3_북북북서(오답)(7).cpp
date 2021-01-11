#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
int get_gcd(int a, int b){
    if(b==0) return a;
    else
        return get_gcd(b, a%b);
}
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		string str;
        cin >> str;
        vector<char> vec;
        int i = 0;
        while(true){
            if(i >= str.size()) break;
            if(str[i] == 'n'){
                vec.push_back('n');
                i += 5;
            }
            if(str[i] == 'w'){
                vec.push_back('w');
                i+=4;
            }
        }

        int a;
       	int n = 1;
        if(vec[vec.size()-1] == 'w'){
            a = 90;
        } else {
            a = 0;
        }

        string res = "";
        for(int i = vec.size()-2; i >= 0; i--){
            int tmp = pow(2,n);
            if( i == 0 ){
                if(vec[i] == 'w'){
                    if((tmp * a + 90) % tmp == 0)
                        a = a + (90 / tmp);
                    else{
                        int gcd = get_gcd(tmp*a+90, tmp);
                        res += to_string((tmp*a + 90)/gcd);
                        res += "/";
                        res += to_string(tmp/gcd);
                    }
                } else {
                    if((tmp * a - 90) % tmp == 0)
                        a = a - (90 / tmp);
                    else{
                        int gcd = get_gcd(tmp*a-90, tmp);
                        res += to_string((tmp*a- 90)/gcd);
                        res += "/";
                        res += to_string(tmp/gcd);
                    }
            	}
            } else {
                if(vec[i] == 'w'){
                    a = a + (90 / tmp);
                } else {
                    a = a - (90 / tmp);
                }
            }
            n++;
        }

        if(res.size() != 0)
            cout << "#" << test_case << " " << res << "\n";
        else
        	printf("%s%d %d\n","#",test_case,a);

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
