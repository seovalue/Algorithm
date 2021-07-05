class Solution {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{13000, 88000, 10000}, new int[]{30, 20}));
    }

    public static int solution(int[] prices, int[] discounts) {
        int answer = 0;
        Arrays.sort(prices);
        Arrays.sort(discounts);

        int j = prices.length - 1;
        for (int i = discounts.length - 1; i >= 0; i--) {
            answer += calculatePrice(prices[j], discounts[i]);
            j--;
        }
        for (int i = 0; i <= j; i++) {
            answer += prices[j];
        }
        return answer;
    }

    private static double calculatePrice(int price, int discount) {
        final double discountRate = (100 - discount) * 0.01;
        return price * discountRate;
    }
}