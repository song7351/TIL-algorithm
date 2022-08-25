def bfs(v, N, t):   # v 시작, N 마지막 정점번호, t 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:      # visit(v)
            return 1    # 목표 발견, 경로의 길이인 경우 visited[99]
        for w in adjList[v]:    # v에 인접하고 방문안한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjList[a].append(b)            # 단방향

    print(f'#{tc} {bfs(0, 99, 99)}')  # 시작, 마지막정점, 목표 정점번호