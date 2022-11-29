# https://www.acmicpc.net/problem/5575

for _ in range(3):
    s_h, s_m, s_s, f_h, f_m, f_s = map(int, input().split())
    
    s_conv = s_h * 3600 + s_m * 60 + s_s
    f_conv = f_h * 3600 + f_m * 60 + f_s
    
    work_time = f_conv - s_conv
    
    w_h = work_time // 3600
    w_m = (work_time - w_h*3600) // 60
    w_s = work_time % 60
    
    print(w_h, w_m, w_s)