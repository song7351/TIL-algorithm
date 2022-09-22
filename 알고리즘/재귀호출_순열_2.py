def f(i, k):
    if i == k:          # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(k):      # 지속적으로 사용기록전부를 확인한다.
            if used[j] == 0:    # a[j]가 사용되었는가?
                used[j] = 1     # 아니라면 사용!
                p[i] = a[j]     # p[i] 값결정
                f(i+1, k)       # 다음 교환진행
                used[j] = 0     # a[j]의 사용취소 why? 다른 자리에서 사용가능하므로

N = 3
a = [i for i in range(1,N+1)]
p = [0] * N
used = [0] * N
f(0,N)
#f(0,10)