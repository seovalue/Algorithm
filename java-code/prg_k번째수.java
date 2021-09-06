import java.util.*;
import java.util.stream.Collectors;

class prg_k번째수 {
    public int[] solution(int[] array, int[][] commands) {
        int index = 0;
        int size = commands.length;
        int[] answer = new int[size];

        for (int i = 0; i < commands.length; i++) {
            int l = commands[i][0] - 1;
            int m = commands[i][1];
            int n = commands[i][2] - 1;

            List<Integer> arrays = Arrays.stream(array).boxed().collect(Collectors.toList());
            arrays = arrays.subList(l, m);
            arrays.sort(Comparator.naturalOrder());
            answer[index] = arrays.get(n);
            index += 1;
        }
        return answer;
    }
}


// 다른 사람의 풀이
//class Solution {
//    public int[] solution(int[] array, int[][] commands) {
//        int[] answer = new int[commands.length];
//        for (int i = 0; i < commands.length; i++) {
//            int[] temp = new int[commands[i][1]-(commands[i][0]-1)];
//            for (int j = 0; j < temp.length; j++) {
//                temp[j] = array[j+(commands[i][0]-1)];
//            }
//            Arrays.sort(temp);
//            answer[i] = temp[commands[i][2]-1];
//        }
//        return answer;
//    }
//}