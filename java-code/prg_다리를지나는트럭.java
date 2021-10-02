import java.util.*;

class prg_다리를지나는트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> bridge = new LinkedList<>();
        List<Integer> arrival = new ArrayList<>();
        int length = truck_weights.length;
        
        int truck, nowWeight = 0; // 현재 트럭, 다리 위의 총 무게
        int index = 0;
        while (arrival.size() != length) {
            answer++;
            
            if (index >= length) {
                truck = 0;
            } else {
                truck = truck_weights[index];
            }
            
            if (bridge.isEmpty()) {
                bridge.offer(truck);
                nowWeight += truck;
                index++;
                continue;
            }
            
            if (bridge.size() == bridge_length) {
                int out = bridge.poll();
                nowWeight -= out;
                if (out != 0) {  
                    arrival.add(out);
                }
            }
            
            if (nowWeight + truck <= weight) {
                bridge.offer(truck);
                nowWeight += truck;
                index++;
            } else {
                bridge.offer(0);
            }
        }
        
        return answer;
    }
}
