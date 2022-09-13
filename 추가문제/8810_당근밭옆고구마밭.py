"""



"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    julgi = 0
    ans_goguma = 0
    ans_cnt = 0
    goguma = lst[0]
    cnt = 1
    for i in range(N-1):
        if lst[i] < lst[i+1]:
            cnt += 1
            goguma += lst[i+1]
            if cnt > ans_cnt:           # 줄기 길이가 길면 무조건 고구마.
                ans_cnt = cnt
                ans_goguma = goguma
            elif cnt == ans_cnt:        # 줄기 길이가 같다면 더 많은 고구마.
                if goguma > ans_goguma:
                    ans_goguma = goguma
            if i == N-2:                # 인덱스가 마지막에 도달하면..
                julgi += 1
        else:
            if cnt > 1:                 # 새로운 줄기가 시작된다면...
                cnt = 1
                julgi += 1
            goguma = lst[i+1]


    print(f'#{tc} {julgi} {ans_goguma}')