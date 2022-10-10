test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2], board[N // 2 - 1][N // 2 - 1] = 1, 1
    board[N // 2][N // 2 - 1], board[N // 2 - 1][N // 2] = -1, -1
    for _ in range(M):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1
        if c == 2:
            c = -1
        board[y][x] = c
        for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            K = 1
            tmp = []
            while K < N:
                ni = y + di * K
                nj = x + dj * K
                K += 1
                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] == -c:
                        tmp.append((ni, nj))
                    elif board[ni][nj] == c:
                        for ti, tj in tmp:
                            board[ti][tj] = c
                        break
                    else:
                        break
                else:
                    break

    # print(board)
    w, b = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b += 1
            elif board[i][j] == -1:
                w += 1

    print(f'#{tc} {b} {w}')