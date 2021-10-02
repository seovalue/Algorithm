import java.util.HashSet;
import org.junit.Test;

public class prg_소수찾기 {
    public void permutation(String prefix, String str, HashSet<Integer> set) {
        int n = str.length();
        if(!prefix.equals("")) {
            set.add(Integer.valueOf(prefix)); //스트링을 Interger로 변환
        }

        for (int i = 0; i < n; i++){
            permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n), set);
        }

    }

    @Test
    public void 순열테스트(){
        permutation("", "17", new HashSet<>());
    }
}
