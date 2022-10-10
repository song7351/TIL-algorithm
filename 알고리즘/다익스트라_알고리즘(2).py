T = int(input())

def dijkstra(N):   # N: 도착지점 # s는 start, 여기서는 0
    d = adjM[0][:]   # s에서 출발해서 다른 정점으로 가는 초기비용
    U = []                      # 비용을 확정짓는곳
    for _ in range(N+1):
        w = 0
        minV = INF
        for i in range(N+1):    # 현재 노드에서 인접 정점중 최소값은?
            if i not in U and minV > d[i]:
                w = i
                minV = d[i]
        U.append(w)
        for v in range(N+1):
            if 0< adjM[w][v] < INF: # 자기 자신이 아니고, 인접한 정점v에 대해서,
                d[v] = min(d[v], d[w]+adjM[w][v])   # 직통으로 가는것과 거쳐서 가는것중에 작은 비용으로 설정해라

    return d[N]



INF = int(1e9)
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjM = [[INF]*(N+1) for _ in range(N+1)]

    for i in range(N+1):    # 자기 자신은 초기화
        adjM[i][i] = 0

    for _ in range(E):      # 인접 행렬 완성!
        s,e,w = map(int, input().split())
        adjM[s][e] = w



    print(dijkstra(N))