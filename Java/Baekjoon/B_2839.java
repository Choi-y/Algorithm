/**
 * 설탕 N 킬로그램 배달 / 3kg, 5kg 봉지 있음
 *  최대한 적은 봉지로 배달
 **/
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main (String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int answer = 10000;

        for (int i = 0; i <= (int)(N/5); i++) {
            int temp = 0;
            if ((N - 5*i) % 3 == 0) {
                temp += i;
                temp += (N - 5*i) / 3;
            }

            if (temp != 0) {
                if (answer > temp) {
                    answer = temp;
                }
            }
        }

        if (answer == 10000) {
            System.out.print(-1);
        }
        else {
            System.out.print(answer);
        }
    }
}