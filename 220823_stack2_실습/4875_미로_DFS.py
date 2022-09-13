"""
N 크기 미로
정답 = 도착: 1 미도착: 0
출발: 2 도착지점: 3
벽 : 1 길 : 0
"""
def Miro(graph1, s, e):
    scheduled_list = [s]
    visited_list = []

    while scheduled_list:
        node = scheduled_list.pop()

        if node not in visited_list:
            visited_list.append(node)
            if node in graph1:
                scheduled_list.extend(graph1[node])

    if e in visited_list:
        return 1
    else:
        return 0

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    start = 0
    end = 0
    graph = {}                              # 노드값을 튜플(좌표)로 설정한다.
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1:            # 벽(==1)이아닌 값들만 노드로 연결한다.
                if (i,j) not in graph:
                    graph[(i,j)] = []
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0<= ni <N and 0<= nj <N and board[ni][nj] != 1:
                            if (ni,nj) not in graph[(i,j)]:
                                graph[(i,j)].append((ni,nj))
            if board[i][j] == 2:
                start = (i,j)
            if board[i][j] == 3:
                end = (i,j)

    ans = Miro(graph, start, end)

    print(f'#{tc} {ans}')