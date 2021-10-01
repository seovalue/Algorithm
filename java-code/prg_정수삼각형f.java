import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class prg_정수삼각형f {

    static int[] dx = new int[]{1, 1};
    static int[] dy = new int[]{0, 1};
    static int maxAnswer = -1;
    static int answer = 0;

    public int solution(int[][] triangle) {
        int length = triangle.length;

        // 방문 배열을 -1로 초기화한다.
        int[][] visit = new int[length][length];
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                visit[i][j] = -1;
            }
        }

        visit[0][0] = triangle[0][0];
        search(triangle, visit, 0, 0, 0);

        return answer;
    }

    private void search(int[][] triangle, int[][] visit, int line, int x, int y) {
        if (line == triangle.length) {
            maxAnswer = Math.max(maxAnswer, answer);
        }

        if (x != 0 && y != 0 && visit[x][y] != -1) { // 이미 방문한 곳
            answer = visit[x][y];
        }

        for (int i = 0; i < 2; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= triangle[line].length || ny >= triangle[line].length) { // 범위를 벗어난 곳
                continue;
            }

            visit[nx][ny] = visit[x][y] + triangle[nx][ny];
            search(triangle, visit, line + 1, nx, ny);
        }
    }

    @Test
    public void 테스트() {
        assertEquals(solution(new int[][]{{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}}), 30);
    }
}
