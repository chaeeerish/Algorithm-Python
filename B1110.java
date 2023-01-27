import java.util.Scanner;

public class B1110 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int copyN = N;
        int count = 0;

        while (true) {
            int left1 = copyN/10;
            int right1 = copyN%10;

            int sumN = left1+right1;
            int left2 = sumN/10;
            int right2 = sumN%10;

            int newN = right1*10+right2;
            copyN = newN;
            count++;

            if (copyN == N) break;
        }

        System.out.println(count);
    }
}
