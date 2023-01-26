    import java.lang.reflect.Array;
    import java.util.*;

public class kakao2019_tuple {


    public static void main(String[] args) {
        Solution2.solution("{{2},{2,1},{2,1,3},{2,1,3,4}}");
        Solution2.solution("{{1,2,3},{2,1},{1,2,4,3},{2}}");
        Solution2.solution("{{20,111},{111}}");
        Solution2.solution("{{123}}");
        Solution2.solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"	);
    }


}

class Solution2 {
    public static boolean isNumeric(String input) {
        try {
            Double.parseDouble(input);
        }
        catch (NumberFormatException e) {
            return false;
        }
        return true;
    }

    public static int[] solution(String s) {
        int[] answer = {};

        String string = s.substring(1, s.length()-1);
        System.out.println("s = " + string);

        ArrayList<String> list = new ArrayList<>();

        int start = 0;
        int end = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '{') {
                start = i;
            } else if (s.charAt(i) == '}') {
                end = i;
                list.add(s.substring(start, end+1));
                System.out.println(s.substring(start, end+1));
                start = 0; end = 0;
            } else {
            }
        }
        list.remove(list.size()-1);
        list.sort((o1, o2) -> o1.length() - o2.length());

        ArrayList<Integer> result = new ArrayList<>();

        for (int i = 0; i < list.size(); i++) {

            s = list.get(i);
            StringBuilder sb = new StringBuilder();
            // "{{20,111},{111}}"
            for (int j = 0; j < s.length(); j++) {
                char a = s.charAt(j);
                if (a == ',') {
                    if (!(result.contains(Integer.valueOf(sb.toString())))) {
                        result.add(Integer.valueOf(sb.toString()));
                    }
                    sb = new StringBuilder("");
                    continue;
                }
                if (a == '"' || a == '{' || a == '}') {
                    continue;
                }
                if (isNumeric(String.valueOf(a)) == true) {
                    sb.append(a);
                    continue;
                }
            }
            if (!(sb.equals(""))) {
                if (!(result.contains(Integer.valueOf(sb.toString())))) {
                    result.add(Integer.valueOf(sb.toString()));
                }
            }
        }
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i) + "\t");
        }
        System.out.println();

        answer = new int[result.size()];
        int i = 0;
        Iterator<Integer> iter = result.iterator(); // set을 Iterator 안에 담기
        while(iter.hasNext()) { // iterator에 다음 값이 있다면
            answer[i] = iter.next();
            i++;
        }


        return answer;
    }
}