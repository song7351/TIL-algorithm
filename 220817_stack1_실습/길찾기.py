"""
출발점은 0, 도착점은 99으로 표현된다.

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호와 길의 총 개수가 주어지고 그 다음 줄에는 순서쌍이 주어진다.

순서쌍의 경우, 별도로 나누어 표현되는 것이 아니라 숫자의 나열이며, 나열된 순서대로 순서쌍을 이룬다.

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
            if end in visited_list:  # 목적지가 방문기록에 있는가?
                return 1

            if node in graph1:                  # 꺼낸 노드가 연결점이 있다면 연결된 노드들을 검색할 리스트에 추가해라.
                scheduled_list.extend(graph1[node])
    return 0

test_case = 10

for tc in range(1, test_case + 1):
    N, E = map(int, input().split())       # N: 테스트케이스 E: 연결노드 개수

    test = list(map(int, input().split()))

    graph = {}                             # key: 노드 value: 연결되 다른 노드리스트
    for i in range(E):
        n1 = test[2*i]
        n2 = test[2*i + 1]

        if n1 not in graph:                # 단방향 그래프.
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

    S = 0
    G = 99                                 # S: 시작노드, G: 도착노드

    ans = Search(graph, S, G)
    print(f'#{tc} {ans}')