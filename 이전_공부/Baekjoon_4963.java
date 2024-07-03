import java.util.ArrayList;
import java.util.Scanner;

public class Baekjoon_4963 {

    public static void dfs(int[][] map, int i, int j) {
        if (i < map.length && i >= 0 && j < map[0].length && j >= 0 && map[i][j] == 1) {
            map[i][j] = 2;
            for (int row: new int[] {i, i-1, i+1}) {
                for (int col: new int[] {j, j-1, j+1}) {
                    dfs(map, row, col);
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> result = new ArrayList<>();

        while(true) {
            int weight = sc.nextInt();
            int height = sc.nextInt();

            if (weight == 0 || height == 0) break;

            int[][] map = new int[height][weight];

            for (int i = 0; i < height; i++) {
                for (int j = 0; j < weight; j++) {
                    map[i][j] = sc.nextInt();
                }
            }

//            for (int i = 0; i < height; i++) {
//                for (int j = 0; j < weight; j++) {
//                    System.out.print(map[i][j] + "\t");
//                }
//                System.out.println();
//            }

//            sc.nextLine();
//            sc.nextLine();

            int count = 0;
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < weight; j++) {
                    if (map[i][j] == 1) {
                        dfs(map, i, j);
                        count++;
                    }
                }
            }

            result.add(count);
//            System.out.println("count = " + count);

        }

        sc.close();

        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }

    }
}
