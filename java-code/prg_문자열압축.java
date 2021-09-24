import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Objects;
import org.junit.jupiter.api.Test;

public class prg_문자열압축 {

    public int solution(String s) {
        if (s.length() == 1) return 1;
        int answer = Integer.MAX_VALUE;
        // aabbccdd -> size 1 ~ 4
        for (int size = 1; size <= s.length() / 2; size++) {
            final String compress = compress(s, size);
            answer = Math.min(compress.length(), answer);
        }
        return answer;
    }

    // s = aabbccdd size = 3 -> aab bcc dd
    // s = aabbccdd size = 1
    private String compress(String s, int size) {
        String base = s.substring(0, size); // base = a
        StringBuilder answer = new StringBuilder();
        int count = 1;
        int index = size; // index = 1;
        while (true) {
            String next = "";
            if (index < s.length() && index + size > s.length()) {
                next = s.substring(index);
                add(base, answer, count);
                add(next, answer, 1);
                break;
            } else {
                next = s.substring(index, index + size); //index = 1, size = 1 -> s.substring(1, 1+1)
            }
            if (Objects.equals(base, next)) {
                count++;
                // 마지막 단어가 이전과 같을 경우
                if (index == s.length() - 1) {
                    answer.append(count).append(base);
                    break;
                }
            } else { // 다르면
                add(base, answer, count);
                base = next;
                count = 1;
            }
            index += size;
            if (index >= s.length()) {
                add(base, answer, count);
                break;
            }
        }
        return answer.toString();
    }

    private void add(String base, StringBuilder answer, int count) {
        if (count == 1) {
            answer.append(base);
        } else {
            answer.append(count).append(base);
        }
    }

    @Test
    public void 정답() {
        assertEquals(7, solution("aabbaccc"));
        assertEquals(9, solution("ababcdcdababcdcd"));
        assertEquals(8, solution("abcabcdede"));
        assertEquals(14, solution("abcabcabcabcdededededede"));
        assertEquals(17, solution("xababcdcdababcdcd"));
    }
}
