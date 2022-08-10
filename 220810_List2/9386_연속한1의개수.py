test_case = int(input())

for tc in range(1,test_case+1):
    N = int(input())
    num_list = list(map(int, input()))
    max_cnt = 0
    cnt = 0
    for i in range(N-1):
        if num_list[i] == num_list[i+1] == 1: # 연속된 1이 나온다면 cnt +1
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        if num_list[i] != num_list[i+1]:      # 두개 연속해서 다르다면 길이는 1이다.
            cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt

    print(f"#{tc} {max_cnt}")