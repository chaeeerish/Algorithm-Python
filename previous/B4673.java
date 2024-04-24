import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class B4673 {
    static Set<Integer> hashSet = new HashSet<>();
    static final int NUMBER = 10000;

    public static void main(String[] args) {
        for (int i = 1; i <= NUMBER; i++) {
            create(i);
        }
//         셀프넘버 == 생성자가 없는 숫자
//         == 누가 나를 안만들어주는
        for (int i = 1; i <= NUMBER; i++) {
            if (!(hashSet.contains(new Integer(i)))) System.out.println(i);
        }

    }

    static void create(int N) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(new Integer(N));
        while(true) {
            int tmp = list.get(list.size()-1);

            // 982
            int a = tmp/1000;
            int b = (tmp%1000)/100; // 9
            int c = ((tmp%1000)%100)/10; // 8
            int d = ((tmp%1000)%100)%10; // 2

            if (tmp+a+b+c+d > NUMBER) break;
            list.add( new Integer(tmp+a+b+c+d));

        }

        list.remove(0);
        if (!(list.isEmpty())) hashSet.addAll(list);
    }
}
