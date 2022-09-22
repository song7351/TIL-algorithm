def f(i, c, N, s):  # i 이동할 구역번호, c 이동횟수, N 총 이동횟수, s 누적 배터리 소비량
    global minV
    if c == N:
        if minV > s:
            minV = s
    else:
        visited[i] = 1
        if sum(visited) == N:  # 남은 구역이 없으면 사무실로 이동
            f(0, c + 1, N, s + arr[i][0])
        else:
            for j in range(1, N):  # 다음에 이동을 고려할 구역
                if visited[j] == 0:  # 방문하지 않은 구역이 있으면 이동
                    f(j, c + 1, N, s + arr[i][j])  # s+arr[i][j] 0~i까지의 소모량 + i에서 j로 가는 소모량
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 100000
    visited = [0] * N
    # visited[0] = 1
    f(0, 0, N, 0)
    print(f'#{tc} {minV}')