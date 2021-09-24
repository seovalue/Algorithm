import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class algo_JUMPGAME {

    static int n;
    static int[][] cache;
    static int[][] array;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int C = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= C; test_case++) {
            n = Integer.parseInt(br.readLine());
            array = new int[n][n];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    array[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            cache = new int[n][n];
            for (int[] arr : cache) {
                Arrays.fill(arr, -1);
            }

            boolean jump = jump(0, 0);
            System.out.println(jump ? "YES" : "NO");
        }
    }

    private static boolean jump(int x, int y) {
        if (x >= n || y >= n) {
            return false;
        }
        if (x == n - 1 && y == n - 1) {
            return true;
        }
        if (cache[x][y] == 1) return false;
        else cache[x][y] = 1;

        int jumpSize = array[x][y];
        return (jump(x + jumpSize, y) || jump(x, y + jumpSize));
    }

    /**
     * step
     * 1. jump(y,x) = (y,x)에서 맨 마지막칸까지 도달할 수 이쓴ㄴ지 여부를 반환한다.
     * (y,x) 위치에 있는 수를 jumpSize라고 하면,
     * 아래쪽으로 뛸 경우 마지막칸에 도달할 수 있는지를 jump(y+jumpSize, x)
     * 오른쪽으로 뛸 경우를 jump(y, x+jumpSize)로 표현할 수 있다.
     * 둘 중 하나만 성공해도 상관없으니
     * jump(y,x) = jump(y+jumpSize,x) || jump(y,x+jumpSize)
     *
     */
}
