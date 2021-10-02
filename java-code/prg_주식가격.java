import java.util.*;
class prg_주식가격 {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        if (prices.length == 1) {
            return answer;
        }
        
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                answer[i]++;
                if (prices[i] > prices[j]) {
                    break;
                } 
            }
        }
        
        return answer;
    }
}
