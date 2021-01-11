#include <iostream>
#include <stdio.h>
using namespace std;

int T;

// 사각형 idx 구하기
int Idx(int y, int x)
{
    return (y/3)*3 + x/3;
}

int main()
{
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        bool flag = true;
        int sdoku[9][9];
        int row[11][11] = {0,};            // 행번호, 숫자
        int col[11][11] = {0,};            // 열번호, 숫자
        int squ[11][11] = {0,};            // 사각형번호, 숫자

        for(int i = 0; i < 9; i++)
        {
            for(int j = 0; j < 9; j++)
            {
                cin >> sdoku[i][j];
            }
        }

        // 행 체크
        for(int i = 0; i < 9; i++)
        {
            for(int j = 0; j < 9; j++)
            {
                int num = sdoku[i][j];
                row[i][num]++;
                if(row[i][num] >= 2)
                {
                    flag = false;
                    break;
                }
            }
            if(flag == false) break;
        }

        // 열 체크
        if(flag)
        {
            for(int j = 0; j < 9; j++)
            {
               for(int i = 0; i < 9; i++)
               {
                  int num = sdoku[i][j];
                  col[j][num]++;
                  if(col[j][num] >= 2)
                  {
                      flag = false;
                      break;
                  }
               }
               if(flag == false) break;
             }
        }


        // 사각형 체크
        if(flag)
        {
            for(int i = 0; i < 9; i++)
            {
                for(int j = 0; j < 9; j++)
                {
                    int num = sdoku[i][j];
                    squ[Idx(i,j)][num]++;
                    if(squ[Idx(i,j)][num] >= 2)
                    {
                        flag = false;
                        break;
                    }
                }
                if(flag == false) break;
            }
        }

        printf("#%d %d\n", t, flag);
    }

    return 0;
}
