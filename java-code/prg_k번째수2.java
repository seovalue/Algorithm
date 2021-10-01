import java.util.*;
class prg_k번째수2 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        List<Integer> arrays = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            arrays.add(array[i]);
        }
        
        for (int l = 0; l < commands.length; l++) {
            int[] command = commands[l];
            int i = command[0];
            int j = command[1];
            int k = command[2];
            
            List<Integer> subList = new ArrayList<>(arrays.subList(i - 1, j));
            Collections.sort(subList);
            answer[l] = subList.get(k - 1);
        }
        return answer;
    }
}
