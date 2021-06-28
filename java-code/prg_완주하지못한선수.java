// 성공 코드
import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String, Integer> hashMap = new HashMap<>();
        
        for (int i = 0; i < phone_book.length; i++) {
            hashMap.put(phone_book[i], i);
        }
        
        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 1; j < phone_book[i].length(); j++) {
                if (hashMap.containsKey(phone_book[i].substring(0,j))) {
                    answer = false;
                    return answer;
                }
            }
        }
        
        return answer;
    }
}

// 3, 4 효율성 실패
/*
import java.util.*; 
class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        for (int i = 0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            }
        }
        return participant[participant.length - 1];
    }
}
*/


// 3, 4 효율성 실패
/*
*
class Solution {
    public boolean solution(String[] phone_book) {
        for (int i = 0; i < phone_book.length - 1; i++) {
            final int hashCodeOfFirst = phone_book[i].hashCode();
            final int sizeOfFirst = phone_book[i].length();
        
            for (int j = i + 1; j < phone_book.length; j++) {
                final int sizeOfSecond = phone_book[j].length();
                final int hashCodeOfSecond = phone_book[j].hashCode();
                
                if (sizeOfFirst <= sizeOfSecond && 
                   isSameHashCode(getHashCode(slice(phone_book[j], sizeOfFirst)), hashCodeOfFirst)) {
                    return false;
                }
                
                if (sizeOfFirst > sizeOfSecond && 
                   isSameHashCode(getHashCode(slice(phone_book[i], sizeOfSecond)), hashCodeOfSecond)) {
                    return false;
                }
            }
        }
        return true;
    }
    
    private String slice(final String str, final int end) {
        return str.substring(0, end);
    }
    
    private int getHashCode(final String number) {
        return number.hashCode();
    }
    
    private boolean isSameHashCode(final int hash1, final int hash2) {
        return hash1 == hash2;
    }
}
 */