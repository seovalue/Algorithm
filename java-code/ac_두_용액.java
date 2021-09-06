import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class ac_두_용액 {
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] solutions = new int[N];
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            solutions[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
        // -99 -2 -1 4 98
        //     i         j
        Arrays.sort(solutions);

        int[] answers = new int[2];
        int i = 0, j = N-1, minSum = Integer.MAX_VALUE;
        while (i < j) {
            int sum = solutions[i] + solutions[j];  // sum : -1
            int temp = sum; // 절댓값 Math.abs()
            if (temp < 0) {
                temp *= -1;
            } // temp: 1
            if (temp < minSum) {
                minSum = temp; // minSum = 1;
                answers[0] = solutions[i];
                answers[1] = solutions[j];
            }

            if (sum > 0) {
                j--;
            } else {
                i++;
            }
        }

        System.out.println(answers[0] + " " + answers[1]);
    }
}
