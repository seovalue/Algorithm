import java.util.*;
class prg_기능개발 {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answers = new ArrayList<>();

        int remainTime = calculateRemainTime(progresses[0], speeds[0]);
        int counts = 1;
        for (int i = 1; i < progresses.length; i++) {
            int nextRemainTime = calculateRemainTime(progresses[i], speeds[i]);
            if (nextRemainTime <= remainTime) {
                counts += 1;
            }
            else {
                remainTime = nextRemainTime;
                answers.add(counts);
                counts = 1;
            }
        }
        if (counts != 0) {
            answers.add(counts);
        }
        return answers.stream().mapToInt(i -> i).toArray();
    }
    
    private int calculateRemainTime(int progress, int speed) {
        int remain = 100 - progress;
        int result = remain / speed;
        if (remain % speed > 0) {
            return result + 1;
        }
        return result;
    }
}

// 다른 사람의 풀이
// public int[] solution(int[] progresses, int[] speeds) {
//	Stack<Integer> stack = new Stack<Integer>();
//
//	for (int i = progresses.length - 1; i >= 0; i--)
//		stack.add((100 - progresses[i]) / speeds[i] + ((100 - progresses[i]) % speeds[i] > 0 ? 1 : 0));
//	List<Integer> s = new ArrayList<Integer>();
//
//	while (!stack.isEmpty()) {
//		int cnt = 1;
//		int top = stack.pop();
//		while (!stack.isEmpty() && stack.peek() <= top) {
//			cnt++;
//			stack.pop();
//		}
//		s.add(cnt);
//	}
//
//	int[] answer = new int[s.size()];
//	for (int i = 0; i < answer.length; i++) {
//		answer[i] = s.get(i);
//	}
//	return answer;
//}