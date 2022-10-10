def dijkstra(N):
    D = [[INF] * N for _ in range(N)]
    U = [[0] * N for _ in range(N)]
    D[0][0] = 0
    for _ in range(N * N):  # 출발점 뺀 N*N-1개의 정점에 대한 비용 결정
        wi, wj = 0, 0  # D[w]가 최소인 w 찾기, U[w]==0
        minV = INF
        for i in range(N):
            for j in range(N):
                if U[i][j] == 0 and minV > D[i][j]:  # 아직 확정되지 않은 칸 중 D가 최소..
                    minV = D[i][j]
                    wi, wj = i, j
        U[wi][wj] = 1  # 현재 D[w]가 최소인 w는 비용 결정
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # w와 인접인 v에 대해 비용 갱신
            vi, vj = wi + di, wj + dj
            if 0 <= vi < N and 0 <= vj < N and U[vi][vj] == 0:
                diff = 1
                if arr[vi][vj] > arr[wi][wj]:
                    diff += arr[vi][vj] - arr[wi][wj]
                D[vi][vj] = min(D[vi][vj], D[wi][wj] + diff)
    return D[N - 1][N - 1]


INF = 1000000000
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {dijkstra(N)}')