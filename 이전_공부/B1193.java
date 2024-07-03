import java.util.ArrayList;
import java.util.Scanner;

public class B1193 {

    static final int N = 100;
    public static void main(String[] args) {

        ArrayList<Integer> listA = new ArrayList<>();
        ArrayList<Integer> listB = new ArrayList<>();

        listA.add(18);
        listB.add(38);

        while(true) {
            listA.add(listA.get(listA.size()-1)+15);
            if (listA.size() > N) break;
        }

        while(true) {
            listB.add(listB.get(listB.size()-1)+34);
            if (listB.size() > N) break;
        }

        for (int i = 0; i < N; i++) {
            if (listB.contains(listA.get(i))) System.out.println( listA.get(i));
        }

//        Scanner sc = new Scanner(System.in);
//        int X = sc.nextInt();
//
//        ArrayList<Integer> sequence = new ArrayList<>();
//        int increase = 2;
//        int initial = 1;
//        int n = 0;
//        sequence.add(initial);
//        while(true) {
//            n = sequence.get(sequence.size()-1)+increase;
//            if (n > X) break;
//            sequence.add(n);
//            increase++;
//        }
//        // X = 10이라면
//        // value    1 3 6 10
//        // index    0 1 2 3
//        // sum      2 3 4 5
//
//        int startIndex = sequence.size()-2;
//        System.out.println("startIndex = " + startIndex);
//        int endIndex = sequence.size()-1;
//        System.out.println("endIndex = " + endIndex);
//        int startValue = sequence.get(startIndex)+1;
//        System.out.println("startValue = " + startValue);
//        int endValue = sequence.get(endIndex);
//        System.out.println("endValue = " + endValue);
//        int sum = endIndex+2;
//        System.out.println("sum = " + sum);
//
//        if ()
//
//
//        for (int i = 0; i < sequence.size(); i++){
//            System.out.println(sequence.get(i));
//        }
    }
}
