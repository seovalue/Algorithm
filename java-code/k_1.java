import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map.Entry;
import java.util.Set;

public class k_1 {

    public static void main(String[] args) {
//        final int[] solution = solution(new String[]{"muzi", "frodo", "apeach", "neo"},
//                                        new String[]{"muzi frodo", "apeach frodo", "frodo neo",
//                                            "muzi neo", "apeach muzi"},
//                                        2);

        final int[] solution = solution(new String[]{"con", "ryan"},
                                        new String[]{"ryan con", "ryan con", "ryan con", "ryan con"},
                                        3);

        for (int i = 0; i < solution.length; i++) {
            System.out.println(solution[i]);
        }
    }

    public static int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        final HashMap<String, Integer> result = new HashMap<>();
        final HashMap<String, Set<String>> reportHistory = new LinkedHashMap<>();

        for (String id : id_list) {
            result.put(id, 0);
            reportHistory.put(id, new HashSet<>());
        }

        for (String r : report) {
            final String[] s = r.split(" ");
            final String source = s[0];
            final String target = s[1];

            if (result.containsKey(target) && !reportHistory.get(source).contains(target)) {
                result.put(target, result.get(target) + 1);
            }
            reportHistory.get(source).add(target);
        }

        int i = 0;
        for (Entry<String, Set<String>> entry : reportHistory.entrySet()) {
            final Set<String> values = entry.getValue();
            int count = 0;
            for (String value : values) {
                if (result.get(value) >= k) {
                    count++;
                }
            }
            answer[i++] = count;
        }
        return answer;
    }
}
