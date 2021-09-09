import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class ac_애너그램 {

    private static boolean solveAnagrams(String first, String second) {
        if (first.length() != second.length()) {
            return false;
        }
        final char[] source = first.toCharArray();
        Arrays.sort(source);
        final char[] target = second.toCharArray();
        Arrays.sort(target);
        return Arrays.equals(source, target);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numTests = sc.nextInt();

        for (int i = 0; i < numTests; i++) {
            String first = sc.next().toLowerCase();
            String second = sc.next().toLowerCase();

            System.out.println(
                first + " & " + second + " are " + (solveAnagrams(first, second) ? "anagrams."
                    : "NOT anagrams."));
        }
    }
}
