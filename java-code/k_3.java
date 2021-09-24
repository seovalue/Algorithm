import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.TreeMap;

public class k_3 {

    public static void main(String[] args) throws ParseException {
//        int[] solution = solution(new int[]{180, 5000, 10, 600},
//                 new String[]{"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"});
        int[] solution = solution(new int[]{120, 0, 60, 591},
                                  new String[]{"16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT",
                                      "18:00 0202 OUT", "23:58 3961 IN"});
//        solution(new int[]{1, 461, 1, 10},
//                 new String[]{"00:00 1234 IN"});

        for (int i = 0; i < solution.length; i++) {
            System.out.println(solution[i]);
        }
    }

    static String DEFAULT_LAST_TIME = "23:59";

    public static int[] solution(int[] fees, String[] records) throws ParseException {
        HashMap<String, String> parkRecord = new HashMap<>();
        TreeMap<Integer, Integer> carFares = new TreeMap<>();

        for (String record : records) {
            final String[] rec = record.split(" ");
            final String nowTime = rec[0];
            final String carNum = rec[1];

            if (parkRecord.containsKey(carNum)) { // 이미 입차한 차가 있다면
                final String inTime = parkRecord.remove(carNum);
                final int accTime = (int) timeBetween(inTime, nowTime);
                final int iCarNum = Integer.parseInt(carNum);
                if (carFares.containsKey(iCarNum)) {
                    carFares.put(iCarNum, carFares.get(iCarNum) + accTime);
                } else {
                    carFares.put(iCarNum, accTime);
                }
            } else {
                parkRecord.put(carNum, nowTime);
            }
        }

        for (Entry<String, String> entry : parkRecord.entrySet()) {
            final int iCarNum = Integer.parseInt(entry.getKey());
            final int accTime = (int) timeBetween(
                entry.getValue(), DEFAULT_LAST_TIME);
            if (carFares.containsKey(iCarNum)) {
                carFares.put(iCarNum, carFares.get(iCarNum) + accTime);
            } else {
                carFares.put(iCarNum, accTime);
            }
        }

        int[] answer = new int[carFares.size()];

        int i = 0;
        for (Entry<Integer, Integer> entry : carFares.entrySet()) {
            System.out.println(entry.getKey());
            answer[i++] = calculateFare(fees, entry.getValue());
        }
        return answer;
    }

    private static int calculateFare(int[] fees, long timeBetween) {
        int time = (int) timeBetween;

        // 요금 기준 초기화
        final int basicTime = fees[0];
        final int basicFare = fees[1];
        final double unitTime = fees[2];
        final int unitFare = fees[3];

        if (time <= basicTime) {
            return basicFare;
        }
        time -= basicTime;
        final double extraUnits = Math.ceil(time / unitTime);
        return (int) (basicFare + (extraUnits * unitFare));
    }

    // 00:00 테스트해보기
    private static long timeBetween(String start, String end) throws ParseException {
        SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm");
        final Date d1 = dateFormat.parse(start);
        final Date d2 = dateFormat.parse(end);

        long diff = d2.getTime() - d1.getTime();
        return diff / 60000;
    }
}
