import java.io.*;
class gr_회문 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            final String string = br.readLine();
            System.out.println(solution(string, 0, string.length() - 1, true));
        }
    }

    private static int solution(String string, int i, int j, boolean chance) {
        while (i < j) {

            char c1 = string.charAt(i);
            char c2 = string.charAt(j);

            if (c1 == c2) {
                i += 1;
                j -= 1;
                continue;
            }

            if (chance) {
                if (solution(string, i + 1, j, false) == 1) {
                    return 1;
                }
                return solution(string, i, j-1, false);
            }

            return 2;
        }

        if (chance) return 0;
        return 1;
    }
}
