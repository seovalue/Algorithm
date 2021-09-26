import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class prg_N으로표현 {
    static int answer = -1;
    public int solution(int N, int number) {
       solve(N, 0, 0, number);
       return answer;

        /*
        +, *, -, / 네 가지의 연산을 할 수 있음.
        n으로 가능한 연산을 모두 수행한 후에는 nn으로 수행함.
        nn = 0;
        nn = nn * 10 + n;
         */
    }

    private void solve(int n, int number, int count, int target) {
        // 기저: 최솟값이 8보다 크면 -1을 리턴한다.
        if (count > 8) {
            return;
        }

        if (number == target) {
            if (answer > count || answer == -1) {
                answer = count;
            }
            return;
        }

        int nn = 0;
        for (int i = 0; i < 8; i++) {
            /**
             * 5 1
             * 55
             * 555
             * ...
             * 55555555
             */
            nn = nn * 10 + n;
            solve(n, number + nn, count + 1 + i, target);
            solve(n, number * nn, count + 1 + i, target);
            solve(n, number / nn, count + 1 + i, target);
            solve(n, number - nn, count + 1 + i, target);
        }
    }

    @Test
    public void 테스트() {
        assertEquals(solution(5, 12), 4);
    }
}
