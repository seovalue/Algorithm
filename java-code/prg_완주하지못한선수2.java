import java.util.*;
class prg_완주하지못한선수2 {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        // players 맵 초기화
        Map<String, Integer> player = new HashMap<>();
        for (String p: participant) {
            if (player.containsKey(p)) {
                player.put(p, player.get(p)+1);
            } else {
                player.put(p, 1);
            }
        }
        
        for (String c: completion) {
            player.put(c, player.get(c)-1);
        }
        
        for (Map.Entry<String, Integer> entry: player.entrySet()) {
            if (entry.getValue() > 0) {
                answer = entry.getKey();
                break;
            }
        }
        
        return answer;
    }
}
