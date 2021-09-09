import java.util.HashMap;
import java.util.Map.Entry;

public class ac_특정단어추출하기 {

    public static void main(String[] args) {
        String line = "Bob hit a ball, the hit BALL flew far after it was hit";

        // 1. 빈 문자열을 기준으로 분리한다.
        String[] words = line.split(" ");

        // 2. HashMap을 하나 선언한다.
        HashMap<String, Integer> map = new HashMap<>();
        for (String word : words) {
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }

        // 3. value가 가장 큰 값을 뽑는다.
        int max = -1;
        String key = "";
        for (Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
                key = entry.getKey();
            }
        }

        System.out.println(key);
    }
}
