public class prg_네트워크 {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visit = new int[n];
        for (int i = 0; i < computers.length; i++) {
            if (visit[i] == 0) {
                dfs(i, computers, visit);
                answer++;
            }
        }

        return answer;
    }

    private int[] dfs(int i, int[][] computers, int[] visit) {
        visit[i] = 1; // 방문했음.

        for (int j = 0; j < computers[0].length; j++) {
            if (i != j && computers[i][j] == 1 && visit[i] == 0)  {
                visit = dfs(j, computers, visit);
            }
        }

        return visit;
    }
}
