import java.util.*;
class prg_위장2 {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        for (String[] c: clothes) {
            String key = c[1];
            String value = c[0];
            
            if (map.containsKey(key)) {
                map.put(key, map.get(key) + 1);
            } else {
                map.put(key, 1);
            }
        }
        
        int answer = 1;
        for (Integer value: map.values()) {
            answer *= (value + 1);
        }
        return answer - 1;
    }
}
