// 듣보잡 (https://www.acmicpc.net/problem/1764)

package Baekjoon;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.StringTokenizer;

public class B_1764 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        // 듣도 못한 사람...
        ArrayList<String> listen = new ArrayList<>(N);
        for (int i=0; i<N; i++) {
            listen.add(br.readLine());
        }

        // 보도 못한 사람 --> 입력과 동시에 체크
        ArrayList<String> answer = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String check = br.readLine();
            if (listen.contains(check)) {
                answer.add(check);
            }
        }

        System.out.println(answer.size());
        Iterator iter = answer.iterator();
        while (iter.hasNext()) {
            System.out.println(iter.next());
        }
    }
}
