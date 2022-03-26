// Base Conversion (https://www.acmicpc.net/problem/11576) 풀이

/**
 * 입력: 진법 A B / 자릿수 / A 이루는 숫자
 */
package Baekjoon;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.lang.Math;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;


public class B_11576 {
    public static void main (String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int m = Integer.parseInt(br.readLine());
        int A_num[] = new int[m];
        
        st = new StringTokenizer(br.readLine());
        for (int i = m-1; i >= 0; i--) {
            A_num[i] = Integer.parseInt(st.nextToken());
        }

        /// 10진법 변환
        int decimal = 0;
        for (int i = 0; i < m; i++) {
            decimal += A_num[i] * Math.pow(A, i);
        }

        // 다시 B 진법으로 변환
        ArrayList<Integer> B_num = new ArrayList<Integer>();
        while (true) {
            B_num.add(decimal%B);

            decimal = (int)(decimal/B);

            if (decimal < B) {
                B_num.add(decimal);

                break;
            }
        }

        Collections.reverse(B_num);

        // 출력
        Iterator iter = B_num.iterator();
        while (iter.hasNext()) {
            System.out.print(iter.next() + " ");
        }
    }
}