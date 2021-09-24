import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import org.junit.Test;

public class prg_후보키 {

    public int solution(String[][] relation) {
        int answer = 0;
        int n = relation[0].length;

        // 1. 가능한 조합을 구해온다. -> 지옥!!
        // 2. 그 조합을 이용해 레코드를 구성하고, 각 레코드를 비교한다.

        for (int r = 1; r <= n; r++) {
            final List<int[]> combs = generateCombinationsIteratively(n, r);
            List<String> records = new ArrayList<>();
            for (int[] comb : combs) {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < r; i++) {
                    for (String[] rel : relation) {
                        sb.append(rel[comb[i]]);
                    }
                }
                records.add(sb.toString());
            }

            int cnt = 0;
            for (int i = 0; i < records.size() - 1; i++) {
                if (Objects.equals(records.get(i), records.get(i + 1))) {
                    cnt++;
                }
            }
            if (cnt == records.size()) {
                answer++;
            }
        }

        return answer;
    }


    // 모르겠어서 검색해옴.
    public List<int[]> generateCombinationsIteratively(int n, int r) {
        List<int[]> combinations = new ArrayList<>();
        int[] combination = new int[r];
        for (int i = 0; i < r; i++) {
            combination[i] = i + 1;
        }
        while (combination[r - 1] < n) {
            combinations.add(combination.clone());
            int t = r - 1;
            while (t != 0 && combination[t] == n - r + t) {
                t--;
            }
            combination[t]++;
            for (int i = t + 1; i < r; i++) {
                combination[i] = combination[i - 1] + 1;
            }
        }
        return combinations;
    }

    @Test
    void 정답() {
        assertEquals(solution(new String[][]{{"100", "ryan", "music", "2"}, {"200", "apeach", "math", "2"},
                         {"300", "tube", "computer", "3"}, {"400", "con", "computer", "4"}, {"500", "muzi", "music", "3"},
                         {"600", "apeach", "music", "2"}}),
                     2);
    }
}
