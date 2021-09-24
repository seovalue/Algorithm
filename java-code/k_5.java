import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

public class k_5 {

    public static void main(String[] args) {
        final int solution = solution(new int[]{0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1},
                                      new int[][]{{0, 1}, {1, 2}, {1, 4}, {0, 8}, {8, 7}, {9, 10},
                                          {9, 11}, {4, 3},
                                          {6, 5}, {4, 6}, {8, 9}});
        System.out.println(solution);
    }

    static class Info {

        List<Integer> children;
        int animal;

        public Info(int animal) {
            this.animal = animal;
            this.children = new ArrayList<>();
        }

        public void addChildren(int number) {
            children.add(number);
        }
    }

    static int count = 0;
    static int maxCount = 0;
    static TreeMap<Integer, Info> nodes;

    public static int solution(int[] info, int[][] edges) {
        nodes = new TreeMap<>();

        for (int i = 0; i < info.length; i++) {
            int animal = 1;
            if (info[i] == 1) {
                animal = -1;
            }
            final Info nodeInfo = new Info(animal);
            nodes.put(i, nodeInfo);
        }

        // 모든 노드 초기화
        for (int i = 0; i < edges.length; i++) {
            int parentNodeNum = edges[i][0];
            int childNodeNum = edges[i][1];

            if (nodes.containsKey(parentNodeNum)) {
                final Info nodeInfo = nodes.get(parentNodeNum);
                nodeInfo.addChildren(childNodeNum);
                nodes.put(parentNodeNum, nodeInfo);
            }
        }

        dfs(0);

        return count;
    }

    private static void dfs(int index) {
        final Info info = nodes.get(index);
        if (count + info.animal == 0) {
            if (count > maxCount) {
                maxCount = count;
            }
            return;
        }
        count += info.animal;

        final List<Integer> children = info.children;

        for (Integer child : children) {
            dfs(child);
        }
    }
}
