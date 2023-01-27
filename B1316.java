import java.util.ArrayList;
import java.util.Scanner;

public class B1316 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String[] strArr = new String[N];
        int result = N;

        for (int i = 0; i < N; i++) {
            strArr[i] = sc.next();
        }
        sc.nextLine();

        for (int i = 0; i < N; i++) {
            ArrayList<Character> charArr = new ArrayList<>();
            for (int j = 0; j < strArr[i].length(); j++) {
                char c = strArr[i].charAt(j);
                if (charArr.isEmpty()) charArr.add(c);
                // ! charArr.isEmpty()
                if (charArr.get(charArr.size()-1) == c) continue;
                else { // !=
                    if (charArr.contains(c)) {
                        result--;
                        break;
                    }
                    else charArr.add(c);
                }

            }
        }
        System.out.println(result);
    }
}
