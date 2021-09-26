import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class algo_FENCE {

    static int[] heights;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int C = Integer.parseInt(bufferedReader.readLine());

        for (int testCase = 1; testCase <= C; testCase++) {
            int N = Integer.parseInt(bufferedReader.readLine());
            StringTokenizer st = new StringTokenizer(bufferedReader.readLine());
            heights = new int[N];
            for (int i = 0; i < N; i++) {
                heights[i] = Integer.parseInt(st.nextToken());
            }
            int result = solve(0, N-1);
            System.out.println(result);
        }
    }

    private static int solve(int leftIndex, int rightIndex) {
        // 기저: 판자가 하나밖에 없는 경우
        if (leftIndex == rightIndex) return heights[leftIndex];

        int mid = (leftIndex + rightIndex) / 2;
        int result = Math.max(solve(leftIndex, mid), solve(mid+1, rightIndex));

        // 두 부분에 걸치는 사각형 중 큰 것 찾기
        int leftPointer = mid;
        int rightPointer = mid + 1;
        int height = Math.min(heights[leftPointer], heights[rightPointer]);

        result = Math.max(result, height * 2);

        while (leftIndex < leftPointer || rightPointer < rightIndex) {
            if (rightPointer < rightIndex &&
                (leftPointer == leftIndex || heights[leftPointer - 1] < heights[rightPointer + 1])) {
                ++rightPointer; // 오른쪽 확장
                height = Math.min(height, heights[rightPointer]);
            } else {
                --leftPointer; // 왼쪽 확장
                height = Math.min(height, heights[leftPointer]);
            }
            // 확장 결과
            result = Math.max(result, height * (rightPointer - leftPointer + 1));
        }

        return result;
    }
}
