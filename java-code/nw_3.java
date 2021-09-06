public class nw_3 {
    public static int solution2(String s, String t) {
        int result = 0;
        while (s.contains(t)) {
            s = s.replaceFirst(t, "");
            result++;
        }
        return result;
    }
}