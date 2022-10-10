"""
마지막 연결지점 번호N과 도로의 개수 E
구간 시작 s, 구간의 끝 지점 e, 구간 거리 w
"""
test_case = int(input())

def dijkstra(start):
    q = [(0,start)] # 시작 노드로가는 최단 경로는 0
    distance[start] = 0

    while q:
        dist, now = q.pop(0)
        if distance[now] < dist:
            continue

        # 현재 노드에서 인접한 노드들을 확인.
        for i in graph[now]:
            cost = dist + i[1]          # 현재 노드를 거쳐 다른 노드로 가는 경우.
            if cost < distance[i[0]]:   # 해당 경우가 기존에 설정된 distance보다 짧다면,
                distance[i[0]] = cost   # 수행하세요.
                q.append((cost, i[0]))

INF = int(1e9)
for tc in range(1, test_case + 1):
    # 노드의 개수, 간선의 개수
    n,m = map(int,input().split())

    # 시작노드
    start = 0

    # 각 노드에 연결되어 있는 노드에 대한 정보
    graph = [[] for i in range(n+1)]

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n+1)

    # 모든 간선 정보 입력
    for _ in range(m):
        s, e, w = map(int,input().split())
        graph[s].append((e,w))

    dijkstra(start)

    print(f'#{tc} {distance[-1]}')