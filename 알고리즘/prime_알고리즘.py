"""
https://gmlwjd9405.github.io/2018/08/30/algorithm-prim-mst.html
"""
test_case = int(input())

def prim1(r,V):
    MST = [0]*(V+1)             # MST 포함여부
    key = [10000]*(V+1)         # 가중치의 최대값 이상으로 초기화.
    key[r] = 0                  # 시작정점의 key
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1

        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v]>0:
                key[v] = min(key[v],adjM[u][v])
    return sum(key)

INF = int(1e9)
for tc in range(1, test_case + 1):
    # 노드의 개수, 간선의 개수
    V,E = map(int,input().split())

    adjM = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        u,v,w = map(int,input().split())
        adjM[u][v] = w
        adjM[v][u] = w

    ans = prim1(0,V)

    print(f'#{tc} {ans}')