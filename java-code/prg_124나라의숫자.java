// 내 풀이
import java.util.*;

public class prg_124나라의숫자 {
   class Solution {
       private static final List<String> BASE_NUMBER = Arrays.asList("4", "1", "2");
       public String solution(int n) {
           List<String> answers = new ArrayList<>();
           while (n != 0) {
               answers.add(0, divide(n));
               n = (n-1) / 3;
           }
           return String.join("",answers);
       }

       private String divide(int n) {
           return BASE_NUMBER.get(n%3);
       }
   }
}


// 다른 사람의 풀이
class Solution {
  public String solution(int n) {
      String[] numbers = {"4", "1", "2"};
      String answer = "";
      
      int num = n;
      
      while(num > 0){
          int remainder = num % 3;
          num /= 3;
          
          if(remainder == 0) num--;
          
          answer = numbers[remainder] + answer;
      }
      
      return answer;
  }
}
 