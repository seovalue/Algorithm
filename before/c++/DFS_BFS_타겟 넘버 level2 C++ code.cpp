#include <string>
#include <vector>
int answer = 0;

using namespace std;
void dfs(vector<int> num, int target, int sum, int depth){
    if(depth == num.size()){
        if(sum == target)
            answer++;
        return;
    }

    dfs(num, target, sum+num[depth], depth+1);
    dfs(num, target, sum-num[depth], depth+1);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers,target,numbers[0],1);
    dfs(numbers,target,numbers[0]*(-1), 1);
    return answer;
}
