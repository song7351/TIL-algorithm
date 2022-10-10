"""
환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)만큼 지불
최소지불금액을 구하라

각 테스트 케이스의 첫 줄에는 섬의 개수 N이 주어지고 (1≤N≤1,000),

두 번째 줄에는 각 섬들의 정수인 X좌표,
세 번째 줄에는 각 섬들의 정수인 Y좌표가 주어진다 (0≤X≤1,000,000, 0≤Y≤1,000,000).
마지막으로, 해저터널 건설의 환경 부담 세율 실수 E가 주어진다 (0≤E≤1).

최소신장트리? - Kruskal 알고리즘
1. 모든 섬과의 연결 정보를 [node1, node2, 비용]으로 정리
2. 무조건 작은거 선택후 사이클을 형성하는지 확인

"""

test_case = int(input())

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)

INF = int(1e9)
for tc in range(1, test_case + 1):
    N = int(input())    # 섬의 개수
    lst_x = list(map(int,input().split()))
    lst_y = list(map(int,input().split()))
    E = float(input())

    edge = []

    for i in range(N):
        for j in range(i+1,N):
            x1,y1 = lst_x[i], lst_y[i]
            x2,y2 = lst_x[j], lst_y[j]
            c = ((x2-x1)**2 + (y2-y1)**2)*E # i번 섬에서 j번 섬으로 이동하는 비용
            edge.append([i,j,c])

    edge.sort(key=lambda x: x[2])   # 비용이 적은 순서로 정렬
    rep = [ i for i in range(N)]    # 각 i번 섬의 root섬 초기화(본인자신)
    cnt = 0                         # 실제 edge에서 선택한 노드의 수   -> 최종적으로는 N-1개
    total = 0

    for u,v,c in edge:                  # 섬1, 섬2, 거리비용
        if find_set(u) != find_set(v):  # 서로 연결이 안되어있다면
            cnt += 1
            union(u,v)                  # 서로 연결해라.
            total += c
            if cnt == N-1:
                break

    print(f'#{tc} {round(total)}')