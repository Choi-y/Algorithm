package Baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Collections;
import java.util.Iterator;

public class B_1764_binary {
    public static void main (String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        ArrayList<String> listen = new ArrayList<>(N);
        for (int i=0; i<N; i++) {
            listen.add(br.readLine());
        }
        ArrayList<String> see = new ArrayList<>();
        for (int i=0; i<M; i++) {
            see.add(br.readLine());
        }

        Collections.sort(listen); Collections.sort(see);

        ArrayList<String> answer = new ArrayList<>();

        if (N > M) {
            for (int i=0; i<M; i++) {
                int idx = Collections.binarySearch(listen, see.get(i));
                if (idx >= 0) {
                    answer.add(listen.get(idx));
                }
            }
        }
        else {
            for (int i=0; i<N; i++) {
                int idx = Collections.binarySearch(see, listen.get(i));
                if (idx >= 0) {
                    answer.add(see.get(idx));
                }
            }
        }
        

        System.out.println(answer.size());
        Iterator iter = answer.iterator();
        while (iter.hasNext()) {
            System.out.println(iter.next());
        }
    }
}
