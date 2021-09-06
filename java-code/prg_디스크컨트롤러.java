import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;

public class prg_디스크컨트롤러 {
    public static void main(String[] args) {
        System.out.println(solution(new int[][]{{0,3},{1,9},{2,6},{30,3}}));
    }

    /**
     * 1. 대기 큐에 모든 작업을 넣고 요청 시간을 기준으로 오름차순
     * 2. 현재 시간 이하의 요청 시간을 가지는 작업을 모두 대기 큐에서 작업큐로 옮긴다.
     * 3. 작업 큐에서 가장 작업시간이 짧은 작업을 꺼내 작업한다.
     */

    public static int solution(int[][] jobs) {
        int answer = 0;
        LinkedList<Job> waitList = new LinkedList<>();
        for (int[] job : jobs) {
            waitList.offer(new Job(job[0], job[1]));
        }
        waitList.sort(Comparator.comparingInt(o -> o.requestTime));
        PriorityQueue<Job> jobQueue = new PriorityQueue<>(Comparator.comparingInt(o -> o.workingTime));

        int now = waitList.peek().requestTime;
        int count = 0;

        while (count < jobs.length) {
            while (!waitList.isEmpty() && waitList.peek().requestTime <= now) {
                jobQueue.offer(waitList.poll());
            }

            if (jobQueue.isEmpty()) {
                now = waitList.peek().requestTime;
                continue;
            }

            Job job = jobQueue.poll();
            answer += (job.workingTime + (now - job.requestTime));
            now += job.workingTime;
            count++;
        }

        return answer / count;
    }

    static class Job {
        int requestTime;
        int workingTime;

        public Job(int requestTime, int workingTime) {
            this.requestTime = requestTime;
            this.workingTime = workingTime;
        }
    }
}
