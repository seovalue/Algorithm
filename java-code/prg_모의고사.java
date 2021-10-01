import java.util.*;
class prg_모의고사 {
    public int[] solution(int[] answers) {
        int[] answer = new int[3];
        int[] num1 = new int[]{1,2,3,4,5};
        int[] num2 = new int[]{2,1,2,3,2,4,2,5};
        int[] num3 = new int[]{3,3,1,1,2,2,4,4,5,5};
        
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == num1[i % num1.length]) {
                answer[0]++;
            }
            if (answers[i] == num2[i % num2.length]) {
                answer[1]++;
            }
            if (answers[i] == num3[i % num3.length]) {
                answer[2]++;
            }
        }
        
        int max = -1;
        for (int i = 0; i < answer.length; i++) {
            max = Math.max(answer[i], max);
        }
        
        List<Integer> results = new ArrayList<>();
        for (int i = 0; i < answer.length; i++) {
            if (answer[i] == max) {
                results.add(i+1);
            }
        }
        return results.stream().mapToInt(i -> i).toArray();
    }
}
