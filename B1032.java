import java.util.Scanner;

public class B1032 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        String[] strArr = new String[N];
        for (int i = 0; i < N; i++) {
            strArr[i] = sc.next();
        }

        StringBuilder result = new StringBuilder();
        for (int j = 0; j < strArr[0].length(); j++) {
            boolean flag = true;
            for (int i = 1; i < N; i++) {
                if(strArr[i-1].charAt(j) != strArr[i].charAt(j)) {
                    flag = false;
                    break;
                }
            }
            if (flag == false)  result.append('?');
            else result.append(strArr[0].charAt(j));
        }

        System.out.println(result.toString());
    }
}
