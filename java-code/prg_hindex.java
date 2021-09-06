import java.util.*;
class prg_hindex {
    public int solution(int[] citations) {
        Arrays.sort(citations); // 오름차순으로 정렬
        int size = citations.length; 
        int start = 0, end = size - 1; // start와 end는 인덱스로 가져간다.
        while (start <= end) { 
            int mid = (start + end) / 2;
            /**
            h번 이상 인용된 논문이 h편 이상인 h의 최댓값
            */
            int h = size - mid;
            if (citations[mid] < h) start = mid + 1;
            else {
                if (mid > 0 && citations[mid] <= h){
                    return h;
                }
                end = mid - 1;
            }
        }
        if (start >= size) {
            return 0;
        }
        if (citations[start] >= size - start) return size - start;
        if (citations[end] >= size - end) return size - end;
        return 0;
    }
}