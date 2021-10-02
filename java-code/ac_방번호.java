import java.io.*;
import java.util.*;
class ac_방번호 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n = br.readLine();
        if (n.length() == 1) {
            System.out.println(1);
            return;
        }

        int[] ints = new int[10];
        for (int i = 0; i < n.length(); i++) {
             int number = n.charAt(i) - '0';
             if (number == 6) { // 6과 9를 한 곳에
                 ints[9]++;
             }
             ints[number]++;
        }

        int set = 0;
        for (int i = 0; i <ints.length; i++) {
            if (i == 9) continue;
            set = Math.max(set, ints[i]);
        }
        int count = ints[9];
        if (count % 2 == 0) {
            set = Math.max(set, count / 2);
        } else {
            set = Math.max(set, (count + 1) / 2);
        }
        System.out.println(set);
    }
}
