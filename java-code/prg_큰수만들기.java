import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class prg_큰수만들기 {

    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();
        int length = number.length();
        int pick = length - k;
        k = pick - 1;

        while (sb.length() != pick) {
            int max = -1;
            int idx = 0;
            for (int i = 0; i < number.length() - k; i++) {
                if (number.charAt(i) - '0' > max) {
                    max = number.charAt(i) - '0';
                    idx = i;
                    if (max == 9) {
                        break;
                    }
                }
            }
            sb.append(max);
            number = number.substring(idx + 1);
            k--;
        }
        /*
        number의 뒤에서부터 k개 제외한 수들 중 가장 큰 값을 뽑아 sb에 저장한다.
        number을 해당 가장 큰 값의 인덱스부터, 마지막까지로 substring한다.
        k를 하나 줄인다.
         */
        return sb.toString();
    }

    @Test
    public void 테스트() {
        assertEquals(solution("1924", 2), "94");
        assertEquals(solution("1231234", 3), "3234");
        assertEquals(solution("4177252841", 4), "775841");
        assertEquals(solution("1111117", 5), "17");
    }
}
