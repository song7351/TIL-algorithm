def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):              # 출발점이 여러개인 경우에도 사용
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(N)}')