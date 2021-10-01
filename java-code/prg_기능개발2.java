import static org.junit.Assert.assertEquals;

import java.util.*;
import org.junit.Test;

public class prg_기능개발2 {
    public int[] solution(int[] progresses, int[] speeds) {
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            int speed = speeds[i];
            int differ = remain / speed;
            if (remain % speed > 0) {
                differ += 1;
            }
            dq.offer(differ);
        }

        List<Integer> answers = new ArrayList<>();
        int answer = 1;
        int first = dq.pop();
        while (!dq.isEmpty()) {
            int next = dq.pop();

            // 하나 남은 경우
            if (next <= first) {
                answer++;
            } else {
                answers.add(answer);
                answer = 1;
                first = next;
            }
            if (dq.isEmpty()) {
                answers.add(answer);
            }
        }

        return answers.stream().mapToInt(i->i).toArray();
    }

    @Test
    public void 테스트() {
        assertEquals(solution(new int[]{93, 30,55}, new int[]{1,30,5}), new int[]{2,1});
    }
}
