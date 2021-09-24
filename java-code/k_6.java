import java.util.Arrays;

class k_6 {

    public int solution(int[][] board, int[][] skill) {
        for (final int[] sk : skill) {
            int degree = sk[5];
            if (sk[0] == 1) {
                degree *= -1;
            }
            destroy(board, sk, degree);
        }

        return (int) Arrays.stream(board)
            .flatMapToInt(Arrays::stream)
            .filter(anInt -> anInt > 0)
            .count();
    }

    private void destroy(int[][] board, int[] skill, int degree) {
        int r1 = skill[1];
        int c1 = skill[2];
        int r2 = skill[3];
        int c2 = skill[4];

        for (int i = r1; i <= r2; i++) {
            for (int j = c1; j <= c2; j++) {
                board[i][j] += degree;
            }
        }
    }
}
