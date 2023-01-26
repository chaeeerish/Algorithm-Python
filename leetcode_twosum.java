import java.lang.reflect.Array;
import java.util.*;

public class leetcode_twosum {

    static class Solution {
        public static int[] twoSum(int[] nums, int target) {
            for (int i = 0; i < nums.length; i++) {
                for (int j = i+1; j < nums.length; j++) {
                    if (nums[i]+nums[j] == target) {
                        System.out.println(i);
                        System.out.println(j);
                        return new int[] {i, j};
                    }
                }
            }
            return new int[] {0, 0};
        }

        public static int[] twoSum2(int[] nums, int target){
            ArrayList<Integer> newNums = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                newNums.add(nums[i]);
            }

//            OptionalInt result = Arrays.stream(nums).filter(a -> a==2).findFirst();
//            System.out.println("result = " + result);
//            System.out.println("result = " + result.getAsInt());
//            return new int[] {0, 0};

            for (int i = 0; i < newNums.size(); i++) {
                int f = target - newNums.get(i);
                int index = newNums.subList(i+1, newNums.size()).indexOf(f);
                if (index != -1) {
                    System.out.println(i);
                    System.out.println(index+i+1);
                    return new int[] {i, index+i+1};
                }
            }
            return new int[] {0, 0};
        }
    }
    public static void main(String[] args) {
        Solution.twoSum2(new int[] {2,7,11,15}, 9);
        Solution.twoSum2(new int[] {3, 2, 4}, 6);
        Solution.twoSum2(new int[] {3, 3}, 6);

    }
}
