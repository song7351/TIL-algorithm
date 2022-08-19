"""
N X N 크기의 단어 퍼즐

특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력

1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)

2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

흰색 부분은 1, 검은색 부분은 0

길이 카운트는 1
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        cnt = 0
        col_cnt = 0
        for j in range(N):
            # 가로행 체크
            if board[i][j] == 1:
                cnt += 1
                if j == N-1 and cnt == K:
                    ans += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
            # 세로열 체크
            if board[j][i] == 1:
                col_cnt += 1
                if j == N-1 and col_cnt == K:
                    ans += 1
            else:
                if col_cnt == K:
                    ans += 1
                col_cnt = 0

    print(f'#{tc} {ans}')