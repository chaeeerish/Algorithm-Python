import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class B1037 {
    public static void main(String[] args) {
        int result = 0;

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        if (N == 1) result = arr[0]*arr[0];
        else {
            Arrays.sort(arr);
            result = arr[0]*arr[arr.length-1];
        }

        System.out.println(result);
    }
}
