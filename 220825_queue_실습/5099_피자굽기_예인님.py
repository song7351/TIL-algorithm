# 피자굽기
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    q = []  # 화덕
    for i in range(N):
        q.append([i + 1, Ci.pop(0)])  # 화덕에 들어간 피자 번호, 피자 치즈 수
    cnt = N + 1
    while len(q) > 0:
        if q[0][1] == 0:  # 치즈가 다 녹았을 경우
            ans = q.pop(0)
            if len(Ci) > 0:  # 아직 덜 구운 피자가 있다면
                q.append([cnt, Ci.pop(0) // 2])  # 화덕에 새로 넣어주기
                cnt += 1
        elif q[0][1] != 0:  # 치즈가 덜 녹았을 경우
            a = q.pop(0)
            a.append(a.pop() // 2)  # 치즈를 절반 녹여주고
            q.append(a)  # 화덕에 append

    print(f'#{tc} {ans[0]}')