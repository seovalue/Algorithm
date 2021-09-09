import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ac_조건정렬 {

    public static void main(String[] args) {
        String[] datum = {"1 A", "1 B", "6 A", "2 D", "4 B"};
        final List<StringPair> stringPairs = Stream.of(datum)
            .map(data -> {
                final String[] s = data.split(" ");
                return new StringPair(s[0], s[1]);
            }).sorted((o1, o2) -> {
                if (o1.s2.compareTo(o2.s2) == 0) {
                    return o1.s1.compareTo(o2.s1);
                }
                return o1.s2.compareTo(o2.s2);
            }).collect(Collectors.toList());

        stringPairs.forEach(
            s -> System.out.println(s.concat())
        );
    }

    public static class StringPair {
        String s1;
        String s2;

        public StringPair(String s1, String s2) {
            this.s1 = s1;
            this.s2 = s2;
        }

        public String concat() {
            return s1 + " " + s2;
        }
    }
}
