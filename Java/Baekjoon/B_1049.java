// 기타줄 (https://www.acmicpc.net/problem/1049)

package Baekjoon;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Collections;

public class B_1049 {
    public static void main (String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 패키지, 낱개 분리
        ArrayList<Integer> pack = new ArrayList<>();
        ArrayList<Integer> each = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            pack.add(Integer.parseInt(st.nextToken()));
            each.add(Integer.parseInt(st.nextToken()));
        }

        // 오름차순 정렬
        Collections.sort(pack); Collections.sort(each);
        
        // 가격 측정
        // 패키지 단위
        int a = (int)(N/6);
        // 낱개 단위
        int b = N%6;
        
        int total = 0;
        // 6개 이상일 때
        if (a != 0) {
            // 패키지 구매가 낱개*6 구매보다 이득인 경우
            if (a * pack.get(0) < a * each.get(0) * 6) {
                total += a * pack.get(0);
            }
            else {
                total += a * each.get(0) * 6;
            }
        }
        // 6개 미만일 경우
        if (b != 0) {
            // 패키지 구매가 낱개*b개 구매보다 이득인 경우
            if (pack.get(0) < each.get(0) * b) {
                total += pack.get(0);
            }
            else {
                total += each.get(0) * b;
            }
        }

        System.out.println(total);
    }
}