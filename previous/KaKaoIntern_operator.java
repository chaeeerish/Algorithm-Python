import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class KaKaoIntern_operator {

    static class Solution {

        public static long solution(String expression) {
            long answer = 0;
            ArrayList<Long> result = new ArrayList<>();

            // string split
            // 짝수 번째는 숫자, 홀수 번째는 operator
            // ex) 0    1   2   3   4
            // ex) 100  -   200 *   300
            StringTokenizer stringTokenizer = new StringTokenizer(expression , "-|\\+|\\*" , true);
            ArrayList<Character> operatorArr = new ArrayList<>();
            ArrayList<Long> operandArr = new ArrayList<>();

            int i = 0;
            while (stringTokenizer.hasMoreTokens()) {
                if (i % 2 == 0) {
                    long tmp = Long.parseLong(stringTokenizer.nextToken());
                    operandArr.add(tmp);
                    System.out.println(operandArr.indexOf(tmp) + ":" + "tmp = " + tmp);
                } else {
                    char tmp = stringTokenizer.nextToken().toString().charAt(0);
                    if (tmp == '+' || tmp == '-' || tmp == '*') operatorArr.add(tmp);
                    System.out.println(operatorArr.indexOf(tmp) + ":" + "tmp = " + tmp);
                }
                i++;
            }

            // 순열을 저장할 arraylist
            ArrayList<String> operatorPer = new ArrayList<>();
            per1(new String[] {"+", "-", "*"}, operatorPer, 0, 3, 3);

            for (String per: operatorPer) {
                // ex) tmp = [-, *, +]
                // 여기서 하나의 result가 나올 것이다.

                // 복제 operator, operand 만들기
                ArrayList<Character> operatorArrCopy = (ArrayList<Character>) operatorArr.clone();
                ArrayList<Long> operandArrCopy = (ArrayList<Long>) operandArr.clone();

                // 진짜 계산 들어가기
                for (int z = 0; z < per.length(); z++) {
                    // ex) tmp.charAt[z] = -
                    // 그러니까 - 먼저 계산 하고 그 다음 쭉쭉쭉

                    // 1. 지금 계산할 연산자
                    Character nowOp = Character.valueOf(per.charAt(z));
                    if (nowOp=='[' || nowOp==']' || nowOp==',' || nowOp==' ') {
                        continue;
                    }

                    /*
                    0:tmp = 100
                    0:tmp = -
                    1:tmp = 200
                    1:tmp = *
                    2:tmp = 300
                    0:tmp = -
                    3:tmp = 500
                    3:tmp = +
                    4:tmp = 20
                     */

                    while (true) {
                        int I = operatorArrCopy.indexOf(nowOp);
                        if (I == -1) break;

                        System.out.println(nowOp + ": " + "인덱스" + I);
                        long A = Long.valueOf(operandArrCopy.get(I));
                        long B = Long.valueOf(operandArrCopy.get(I+1));
                        long R = compute(A, B, nowOp);

                        operandArrCopy.remove(I);
                        operandArrCopy.remove(I);
                        operatorArrCopy.remove(I);

                        operandArrCopy.add(I, new Long(R));
                    }

                }
                // 이 반복문 끝내고 나오면 이제 최종 결과만 남았겠지
                Long L = new Long(Math.abs(operandArrCopy.get(0).longValue()));
                result.add(L);
            }

            answer = Collections.max(result).longValue();
            return answer;
        }
    }

    static long compute(long A, long B, char operator) {
        if (operator == '+') return A+B;
        else if (operator == '-') return A-B;
        else if (operator == '*') return A*B;
        else return 0;
    }

    static void per1(String[] arr, ArrayList<String> operatorPer, int depth, int n, int r) {
        if(depth == r) {
            // print(arr, r);
            operatorPer.add(Arrays.toString(arr));
            return;
        }

        for(int i = depth; i < n; i++) {
            swap(arr, depth, i);
            per1(arr, operatorPer, depth + 1, n, r);
            swap(arr, depth, i);
        }
    }

    static void swap(String[] arr, int depth, int i) { //두 배열의 값을 바꾸는 Swap 함수
        String temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }

    public static void main(String[] args) {
        System.out.println(Solution.solution("100-200*300-500+20"));
        System.out.println(Solution.solution("50*6-3*2"));
    }
}
