#include<iostream>
#include <set>
using namespace std;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int visit[9][9];
bool chkSquare(int sudoku[9][9], int start, int x, int y){
    int loc = 0;
    set<int> square;
    for(int i = 0; i < 9; i++){
        square.clear();
        x = (i % 3) * 3;
        y = (i / 3) * 3;
        square.insert(sudoku[y][x]);
        visit[y][x] = 1;
        int cnt = 1, max_width = x+3, max_height =y+3;
        while(true){
            if(x+dx[loc] >= 0 && y+dy[loc] >= 0 && x+dx[loc] < max_width && y +dy[loc] <max_height && !visit[y+dy[loc]][x+dx[loc]]){
                x += dx[loc];
                y += dy[loc];
                square.insert(sudoku[y][x]);
                visit[y][x] = 1;
                cnt++;
            }else{
                if(loc == 3) loc = 0;
                else loc++;
            }
            if(cnt == 9) break;
        }
        if(square.size() != 9){
            square.clear();
            return false;
		}
    }
    return true;
}
bool chkGaro(int sudoku[9][9], int start, int x, int y){
    set<int> garo;
    for(int i = 0; i < 9; i++){
        garo.clear();
        garo.insert(sudoku[y][x]);
        for(int j = 0; j < 9; j++){
             if(x + dx[0] >= 0 && x + dx[0] < 9){
                x += dx[0];
                garo.insert(sudoku[y][x]);
        	}
    	}
        if(garo.size() != 9) {
            garo.clear();
            return false;
        }
        y++; x= 0;
    }
    return true;
}
bool chkSero(int sudoku[9][9], int start, int x, int y){
    set<int> sero;
    for(int i = 0; i < 9; i++){
        sero.clear();
        sero.insert(sudoku[y][x]);
        for(int j = 0; j < 9; j++){
             if(y + dy[1] >= 0 && y + dy[1] < 9){
                y+=dy[1];
                sero.insert(sudoku[y][x]);
        	}
    	}
        if(sero.size() != 9){
            sero.clear();
            return false;
        }
        x++; y = 0;
    }
    return true;
}
int main(int argc, char** argv)
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int sudoku[9][9] = {0};
      	visit[9][9] = {0};
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                cin >> sudoku[i][j]; //스도쿠 초기화
            }
        }

        if(chkGaro(sudoku,0,0,0) == true && chkSero(sudoku,0,0,0) == true && chkSquare(sudoku,0,0,0) == true)
        {
            cout << "#" << test_case << " 1\n";
        }
        else{
            cout << "#" << test_case << " 0\n";
        }

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
