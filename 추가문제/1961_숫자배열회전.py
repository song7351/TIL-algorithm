"""
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

N은 3 이상 7 이하이다.
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    ans_board = [[''] * 3 for _ in range(N)]

    for i in range(3):                                  # 보드는 3번돌린다.
        new_board = [['']*N for _ in range(N)]
        for k in range(N):
            for l in range(N):
                new_board[k][l] = board[N-l-1][k]
        board = new_board                               # 90도 돌려서 저장
        for j in range(N):
            ans_board[j][i] = ''.join(board[j])

    print(f'#{tc}')
    for i in range(N):
        for j in range(3):
            print(ans_board[i][j], end=" ")
        print()
    print()