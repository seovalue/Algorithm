import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class prg_정수삼각형 {

    public int solution(int[][] triangle) {
        int[][] memo = new int[triangle.length][triangle.length];
        memo[0][0] = triangle[0][0];

        for (int i = 1; i < triangle.length; i++) {
            memo[i][0] = triangle[i][0] + memo[i - 1][0];

            for (int j = 1; j < i + 1; j++) {
                memo[i][j] = triangle[i][j] + Math.max(memo[i - 1][j - 1], memo[i - 1][j]);
            }
        }

        int max = 0;
        for (int i = 0; i < memo[memo.length - 1].length; i++) {
            max = Math.max(memo[memo.length - 1][i], max);
        }

        return max;
    }

    @Test
    public void 테스트() {
        assertEquals(solution(new int[][]{{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}}), 30);
    }
}
