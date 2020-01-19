//SW 8821 D3 문자열
#include<iostream>
#include <string>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		string input, output="";
        cin >> input;
        for(int i = 0; i < input.size(); i++)
        {
            if(output.length() == 0)
            {
                output+=input[i];
            }
            else{
            	int idx = output.find(input[i]);
                if(idx == -1)
                {
                    output += input[i];
                }
                else if(idx != -1)
                {
                    if(output.length() == 1)
                    {
                        output.resize(0);
                    }
                    else
                    {
                        for(int j = idx+1; j < output.length(); j++)
                        {
                            output[j-1]=output[j];
                        }
                        output.resize(output.size()-1);
                    }
                }
            }
        }
        cout <<"#"<<test_case<<" "<<output.length() <<"\n";
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
