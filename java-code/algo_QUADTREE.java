import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class algo_QUADTREE {
    static int N, pointer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= N; testCase++) {
            pointer = -1;
            String input = br.readLine();
            System.out.println(recursive(input));
        }
    }

    private static String recursive(String input) {
        pointer++;
        char ch = input.charAt(pointer);
        if (ch == 'b' || ch == 'w') {
            return String.valueOf(ch);
        }

        String leftUp = recursive(input);
        String rightUp = recursive(input);
        String leftDown = recursive(input);
        String rightDown = recursive(input);

        return "x" + leftDown + rightDown + leftUp + rightUp;
    }
}
