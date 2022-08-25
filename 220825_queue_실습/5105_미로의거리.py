"""
N = 미로의 크기
최소한의 이동회수는? 없으면 0
출발 2, 도착 3
"""
def BFS(start, end):
    visited_list = [[-1]*N for _ in range(N)]   # 방문할때 깊이가 1씩증가. 시작점은 제외해야되므로 -1부터 시작
    lst = [start]
    visited_list[start[0]][start[1]] = 0

    while lst:
        x = lst.pop(0)
        if visited_list[x[0]][x[1]] != -1:
            if x in graph:
                for y in graph[x]:
                    if y in graph:
                        if visited_list[y[0]][y[1]] == -1:
                            visited_list[y[0]][y[1]] = visited_list[x[0]][x[1]] + 1
                            lst.append(y)
            if x == end:
                return visited_list[x[0]][x[1]]-1   # 도착지점도 제외해야되므로 -1.
    return 0


test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    # 시작점 설정
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                s = (i,j)
            if miro[i][j] == 3:
                e = (i,j)

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    graph = {}          # 벽이 아닌 노드들을 연결
    for i in range(N):
        for j in range(N):
            if miro[i][j] != 1:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<= ni< N and 0<= nj <N and miro[ni][nj] != 1:
                        if (i,j) not in graph:
                            graph[(i,j)] = [(ni,nj)]
                        elif (ni,nj) not in graph[(i,j)]:
                            graph[(i, j)].append((ni,nj))

    ans = BFS(s,e)

    print(f'#{tc} {ans}')
