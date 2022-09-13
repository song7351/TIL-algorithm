"""
출발노드에서 도착노드까지 최소거리
1줄: 테스트케이스 개수
2줄: V E // V: 노드범위(1~V) E: 노드연결 개수
E개줄: n1 n2 // n1 - n2 노드연결(양방향)
마지막줄: S G // 시작도착
"""
def BFS(start, end):
    visited_lst = [-1] * (V+1)      # 시작노드는 제외해야되므로 -1부터 시작
    lst = [start]
    visited_lst[start] = 0
    while lst:
        node = lst.pop(0)
        if visited_lst[node] != -1 and graph[node]:
            for x in graph[node]:
                if visited_lst[x] == -1:
                    visited_lst[x] = visited_lst[node] + 1
                    lst.append(x)
                if x == end:
                    return visited_lst[x]
    return 0

test_case = int(input())

for tc in range(1, test_case + 1):
    V, E = map(int, input().split())
    graph = {}
    for i in range(E):
        n1, n2 = map(int, input().split())

        # 양방향 노드설정
        if n1 not in graph:
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        elif n1 not in graph[n2]:
            graph[n2].append(n1)

    S, G = map(int, input().split())

    ans = BFS(S,G)

    print(f'#{tc} {ans}')