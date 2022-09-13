"""
 1 2 3
 4 a 5
 3 2 1

 a = 3
 착륙지점 (a)를 기준으로 주변 8칸 이내 a보다 작은 수가 4개 이상일때, a는 착륙 가능

 이때 착륙가능한 지역의 수는?
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())    # 세로N, 가로M
    board = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0, -1, -1, 1, 1]    #상하좌우 좌상단 우상단 좌하단 우하단
    dj = [0, 0, -1, 1, -1, 1, -1, 1]

    ans = 0
    for i in range(N):
        for j in range(M):
            x = board[i][j]
            cnt = 0
            for k in range(8):          #8방면 비교.
                ni = i + di[k]
                nj = j + dj[k]
                if 0<= ni< N and 0<= nj< M and board[ni][nj] < x:
                    cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')
