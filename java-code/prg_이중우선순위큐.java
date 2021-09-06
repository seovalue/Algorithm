import java.util.Arrays;
import java.util.Comparator;
import java.util.Objects;
import java.util.PriorityQueue;

public class prg_이중우선순위큐 {
    public static void main(String[] args) {
//        System.out.println(Arrays.toString(solution(new String[]{"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"})));
//        System.out.println(Arrays.toString(solution(new String[]{"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"})));
//        System.out.println(Arrays.toString(solution(new String[]{"I 4", "I -1", "I 6", "I 3"})));
//        System.out.println(Arrays.toString(solution(new String[]{"I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"})));
//        System.out.println(Arrays.toString(solution(new String[]{"I 5", "I 5", "D 1", "I 7", "D -1", "I 8"})));
        System.out.println(Arrays.toString(solution(new String[]{"D 1", "D -1", "I 0", "I -1", "I 0"})));
    }

    public static int[] solution(String[] operations) {
        int[] answer = {0,0};
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (String op : operations) {
            String[] operation = op.split(" ");

            if (operation[0].equals("I")) {
                maxHeap.add(Integer.parseInt(operation[1]));
                minHeap.add(Integer.parseInt(operation[1]));
            }

            if (operation[0].equals("D")) {
                if (!maxHeap.isEmpty()) {
                    if (operation[1].equals("1")) {
                        int max = maxHeap.peek();
                        maxHeap.remove(max);
                        minHeap.remove(max);

                    } else { // -1
                        int min = minHeap.peek();
                        maxHeap.remove(min);
                        minHeap.remove(min);
                    }
                }
            }

        }
        if (!maxHeap.isEmpty()) {
            answer[0] = maxHeap.peek(); // 큰 값
            answer[1] = minHeap.peek(); // 작은 값
        }
        return answer;
    }
}
