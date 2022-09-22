"""
NxN 칸에 숫자가 적힌 판이 주어지고,
각 칸에서는 오른쪽이나 아래로만 이동
1줄: 테스트케이스
2줄: N        3<=N<=13
N줄: 숫자판
"""
def f(i, N, n, x,y):
    global ans
    if i == N:          # 최대 이동횟수에 도달하면,
        if n < ans:     # 최소합인지 비교해라.
            ans = n
    else:
        if 0<= x <len(board) and 0<= y < len(board):            # 이동하는 좌표가 범위 안인가?
            n += board[x][y]
            # 오른쪽으로 이동
            if 0<= x+1 <len(board) and 0<= y < len(board):
                f(i+1, N, n, x+1, y)
            # 아래로 이동
            if 0 <= x < len(board) and 0 <= y < len(board):
                f(i+1, N, n, x, y+1)

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 240
    x,y = 0,0
    # 현재 이동횟수, 최대이동횟수, 최소합, 좌표x,좌표y
    f(0, (N-1)*2,board[N-1][N-1], x,y)
    print(f'#{tc} {ans}')