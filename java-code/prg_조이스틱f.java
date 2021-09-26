import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class prg_조이스틱f {
    public int solution(String name) {
        int answer = 0;

        int length = name.length();
        int minMove = length - 1;
        for (int i = 0; i < length; i++) {
            answer += calculateAlphabetDistance(name.charAt(i));

            int next = i+1;
            while (next < length && name.charAt(next) == 'A') {
                next++;
            }

            // 내 위치 (i)에서 처음 위치 (i)로 돌아간 다음, A가 연속으로 나오는 지점의 다음(next)을 끝(length)에서 계산해준다.
            minMove = Math.min(minMove, i + i + length - next);
        }

        answer += minMove;
        return answer;
    }

    private int calculateAlphabetDistance(char alpha) {
        if (alpha == 'A') return 0;
        return Math.min(Math.abs(alpha - 'A'), Math.abs(alpha - 'Z') + 1);
    }

    @Test
    public void 테스트() {
        assertEquals(solution("JAZ"), 11);
    }
}
