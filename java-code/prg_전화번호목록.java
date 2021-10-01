// 효율성 시간 초과
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for (int i = 0; i < phone_book.length; i++) {
            String number = phone_book[i];
            for (int j = i + 1; j < phone_book.length; j++) {
                if (phone_book[j].startsWith(number)) {
                    return false;
                }
            }
        }
        return true;
    }
}

// 효율성 통과
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < phone_book.length; i++) {
            map.put(phone_book[i], i);
        }
        
        for (String key: map.keySet()) {
            for (int i = 1; i < key.length(); i++) {
                if (map.containsKey(key.substring(0, i))) {
                    return false;
                }
            }
        }
        
        return true;
    }
}
