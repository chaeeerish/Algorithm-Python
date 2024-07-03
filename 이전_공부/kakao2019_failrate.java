import java.util.ArrayList;
import java.util.Collections;


class Stage implements Comparable<Stage> {
    int number;
    int total;
    int now;
    double failrate;

    public Stage(int number, int count, int now, double failrate) {
        this.number = number;
        this.total = count;
        this.now = now;
        this.failrate = failrate;
    }

    public void calculate() {
        if (this.total == 0) {
            this.failrate = 0.0d;
            return;
        }
        if (this.now == 0) {
            this.failrate = 0.0d;
            return;
        }
        this.failrate = (double)this.now / (double)this.total;
    }

    @Override
    public int compareTo(Stage o) {

        if (Double.compare(o.failrate, this.failrate) == 0) {
            if (o.number > this.number) return -1;
            else return 1;
        } else if (Double.compare(o.failrate, this.failrate) > 0) {
            return 1;
        } else {
            return -1;
        }
    }
}

class Solution {
    public static int[] solution(int N, int[] stages) {
        int[] answer = {};

        answer = new int[N];

        ArrayList<Stage> stageList = new ArrayList<>();
        for (int i = 0; i < N+1; i++) {
            Stage tmp = new Stage(i, 0, 0, 0.0d);
            stageList.add(tmp);
        }

        // total 초기화
        for (int i = 0; i < stages.length; i++) {
            stages[i]--;
            for (int j = 0; j <= stages[i]; j++) {
                stageList.get(j).total++;
            }
        }

        // count 초기화
        for (int i = 0; i < stages.length; i++) {
            stageList.get(stages[i]).now++;
        }

        // failrate 계산
        for (int i = 0; i < N+1; i++) {
            stageList.get(i).calculate();
        }

        stageList.remove(stageList.size()-1);


        // 정렬
        Collections.sort(stageList);

        for (int i = 0; i < N; i++) {
            // System.out.println("stageList.get(i).number = " + stageList.get(i).number);
            answer[i] = stageList.get(i).number+1;
            System.out.print(answer[i] + "\t");
        }

        return answer;
    }
}


public class kakao2019_failrate {
    public static void main(String[] args) {
        Solution.solution(5, new int[] {2, 1, 2, 6, 2, 4, 3, 3});
    }
}
