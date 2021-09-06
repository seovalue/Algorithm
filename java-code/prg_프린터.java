import java.util.*;
class prg_프린터 {
    public int solution(int[] priorities, int location) {
        Queue<Pair> queue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new Pair(i, priorities[i]));
        }

        int answer = 0;
        while(!queue.isEmpty()) {
            boolean isPrior = true;
            final int priority = queue.peek().priority;
            for (Pair p : queue) {
                if (p.priority > priority) {
                    isPrior = false;
                    break;
                }
            }

            final Pair pair = queue.poll();
            if (isPrior) { // 더 큰 우선순위가 존재하지 않으면
                answer += 1;
                if (pair.idx == location) {
                    break;
                }
            } else {
                queue.offer(pair); // 다시 뒤에 집어넣음!
            }
        }
        return answer;
    }

    class Pair {
        int idx;
        int priority;

        Pair(int idx, int priority) {
            this.idx = idx;
            this.priority = priority;
        }
    }
}