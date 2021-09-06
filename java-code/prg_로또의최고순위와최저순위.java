import java.util.*;

class prg_로또의최고순위와최저순위 {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[]{1, 6}; // 모두 0인 경우를 default로 둔다.
        List<Integer> lottoList = new ArrayList<>();
        for (int lotto : lottos) {
            lottoList.add(lotto);
        }
        final int size = lottoList.size();
        final int zeros = Collections.frequency(lottoList, 0);
        
        if (zeros == size) {
            return answer;
        }
        
        int lowestRank = 0;
        for (int win_num : win_nums) {
            if (lottoList.contains(win_num)) { // 우승 번호를 갖고 있다면
                lowestRank += 1;
            }
        }
        final int highestRank = zeros + lowestRank;
        answer[0] = convertToRank(highestRank);
        answer[1] = convertToRank(lowestRank);
        return answer;
    }
    
    private int convertToRank(final int counts) {
        if (counts == 1 || counts == 0) {
            return 6;
        }
        return 7 - counts;
    }
}