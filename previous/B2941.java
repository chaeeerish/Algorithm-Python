import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class B2941 {
    public static void main(String[] args) {
        /*
        č	c=
        ć	c-
        dž	dz=
        đ	d-
        lj	lj
        nj	nj
        š	s=
        ž	z=
         */

        Scanner sc = new Scanner(System.in);
        String input = sc.next(); // ex) ljes=njak

        HashMap<String, String> hashMap = new HashMap<>();
        hashMap.put("č", "c=");
        hashMap.put("ć", "c-");
        hashMap.put("dž", "dz=");
        hashMap.put("đ", "d-");
        hashMap.put("lj", "lj");
        hashMap.put("nj", "nj");
        hashMap.put("š", "s=");
        hashMap.put("ž", "z=");

        ArrayList<String> alphabet = new ArrayList<>();

        int count = 0;
        for (int i = 0; i < input.length(); i++) {
            if (i+2 < input.length()) {
                if (hashMap.containsValue(input.substring(i, i+3))) {
                    alphabet.add(input.substring(i, i + 3));
                    i++; i++;
                }
                else if (hashMap.containsValue(input.substring(i, i+2))) {
                    alphabet.add(input.substring(i, i + 2));
                    i++;
                } else alphabet.add(input.substring(i, i + 1));
            } else if (i+1 < input.length()) {
                if (hashMap.containsValue(input.substring(i, i+2))) {
                    alphabet.add(input.substring(i, i + 2));
                    i++;
                } else alphabet.add(input.substring(i, i + 1));
            } else {
                alphabet.add(input.substring(i, i + 1));
            }
        }

        System.out.println(alphabet.size());

    }
}
