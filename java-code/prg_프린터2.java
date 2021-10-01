import java.util.*;
class prg_프린터2 {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Deque<Pair> priorityDeque = new ArrayDeque<>();
        for (int i = 0; i < priorities.length; i++) {
            priorityDeque.offer(new Pair(priorities[i], i));
        }
        
        Arrays.sort(priorities);
        int index = priorities.length - 1;
        
        int order = 1;
        while (!priorityDeque.isEmpty()) {
            Pair pair = priorityDeque.pop();
            if (pair.priority < priorities[index]) {
                priorityDeque.offer(pair);
                continue;
            }
            if (pair.index == location) {
                answer = order;
                break;
            }
            order++;
            index--;
        }
        
        return answer;
    }
    
    class Pair {
        int priority;
        int index;
        
        Pair (int priority, int index) {
            this.priority = priority;
            this.index = index;
        }
    }
}
