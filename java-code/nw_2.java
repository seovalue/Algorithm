import java.util.ArrayList;
import java.util.List;

class nw_2 {
    public static void main(String[] args) {
        final String[] strings = solution("abcxxxxyzzzzzzxxxxyabc");
        for (String s : strings) {
            System.out.println(s);
        }
    }

    public static String[] solution(String s) {
        List<String> frontValues = new ArrayList<>();
        List<String> backValues = new ArrayList<>();
        int i = 1;
        while (i < s.length()) {
            String front = s.substring(0, i);
            String back = s.substring(s.length() - i);

            if (front.equals(back)) {
                frontValues.add(front);
                backValues.add(0, back);
                s = s.substring(i, s.length() - i);
                i = 0;
            }
            i += 1;
        }

        if (!s.equals("")) {
            frontValues.add(s);
        }
        frontValues.addAll(backValues);
        return frontValues.toArray(new String[0]);
    }
}
