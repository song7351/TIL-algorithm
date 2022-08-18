"""
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,

두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.
"""
def Search(graph1, start, end):
    scheduled_list = [start]
    visited_list = []

    if start not in graph1:                     # 만약 시작노드가 그래프에 없다면(연결점이 없다면) 0
        return 0

    while scheduled_list:
        node = scheduled_list.pop()

        if node not in visited_list:            # 꺼낸노드가 연결점이 있고 방문 기록이 없다면, 방문기록 남겨라
            visited_list.append(node)
            if node in graph1:                  # 꺼낸 노드가 연결점이 있다면 연결된 노드들을 검색할 리스트에 추가해라.
                scheduled_list.extend(graph1[node])

    if end in visited_list:                     # 목적지가 방문기록에 있는가?
        return 1
    else:
        return 0

test_case = int(input())

for tc in range(1, test_case + 1):
    V, E = map(int, input().split())       # V: 정점개수 E: 연결노드 개수

    graph = {}                             # key: 노드 value: 연결되 다른 노드리스트
    for i in range(E):
        n1, n2 = map(int, input().split())

        if n1 not in graph:                # 단방향 그래프.
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

        """
        # 양방향일 경우, 추가
        if n2 not in graph:
            graph[n2] = [n1]
        elif n1 not in graph[n2]:
            graph[n2].append(n1)
        """

    S, G = map(int, input().split())       # S: 시작노드, G: 도착노드

    ans = Search(graph, S, G)
    print(f'#{tc} {ans}')