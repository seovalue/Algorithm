import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import org.junit.Test;

public class prg_구명보트 {

    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        Deque<Integer> boat = new LinkedList<>();
        for (Integer person : people) {
            boat.offer(person);
        }

        int currWeight;
        int size = 0;
        while (!boat.isEmpty()) {
            currWeight = boat.pollLast(); // 가장 큰 값을 뽑는다.
            answer++;

            if (boat.isEmpty()) {
                break;
            }
            // 가장 큰 무게와 가장 작은 무게를 더했는데 무게 제한보다 작은 경우
            if (currWeight + boat.getFirst() <= limit) {
                boat.pollFirst();
            }
        }
        return answer;
    }

    @Test
    public void 테스트() {
//        assertEquals(solution(new int[]{70,50,80,50}, 100), 3);
//        assertEquals(solution(new int[]{70,50,80}, 100), 3);
//        assertEquals(solution(new int[]{40, 50, 60, 90}, 100), 3);
//        assertEquals(solution(new int[]{40, 40, 40}, 100), 2);
//        assertEquals(solution(new int[]{40, 50, 150, 160}, 200), 2);
        assertEquals(solution(new int[]{100, 500, 500, 900, 950}, 1000), 3);
    }
}
