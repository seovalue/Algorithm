class k_2 {

    public static void main(String[] args) {
//        System.out.println(solution(437674, 3));
        System.out.println(solution(2, 10));
    }

    // P0
    // 0P
    // 0P0

    public static int solution(int n, int k) {
        int answer = 0;
        String nNumber = "";
        if (k == 10) { // 10진수의 경우에는 변환할 필요가 없다.
            nNumber = String.valueOf(n);
        } else {
            nNumber = convert(n, k);
        }
        final String[] split = nNumber.split("0");

        for (String s : split) {
            if (!s.isEmpty() && isPrime(Long.parseLong(s))) {
                answer++;
            }
        }
        return answer;
    }

    private static String convert(int n, int k) {
        StringBuilder result = new StringBuilder();
        while (n > 0) {
            result.insert(0, (n % k));
            n = n / k;
        }
        return result.toString();
    }

    private static boolean isPrime(long n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
