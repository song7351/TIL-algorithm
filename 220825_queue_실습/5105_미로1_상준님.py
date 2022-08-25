# dfs풀이

def dfs(x, y):
    global cnt
    if P[x][y] == 0 or P[x][y] == 2:
        P[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        P[x][y] = 0
    elif P[x][y] == 3:
        cnt = 1
        return


for _ in range(1, 11):
    tc = int(input())
    P = [list(map(int, input())) for _ in range(16)]
    cnt = 0
    visited = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if P[i][j] == 2:
                dfs(i, j)
                break
        if P[i][j] == 2:
            break

    print(f'#{tc} {cnt}')