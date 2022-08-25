"""
총 10개의 테스트케이스가 주어진다.

미로 크기는 16 * 16
가로방향을 x 방향, 세로방향을 y 방향
길 0
벽 1
시작 2
도착 3
도착 가능한가? 예 1 아니오 0
"""
def BFS(start, end):
    visited_lst = [[0]*N for _ in range(N)]
    lst = [start]
    visited_lst[start[0]][start[1]] = 1
    while lst:
        x = lst.pop(0)
        if visited_lst[x[0]][x[1]] != 0:
            if x in graph:
                for w in graph[x]:
                    if w == end:
                        return 1
                    if visited_lst[w[0]][w[1]] == 0 and w in graph:
                        visited_lst[w[0]][w[1]] = visited_lst[x[0]][x[1]] + 1
                        lst.append(w)
    return 0

test_case = 10

for tc in range(1, test_case + 1):
    test = int(input())
    N = 16
    miro = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                s = (i,j)
            if miro[i][j] == 3:
                e = (i,j)

    di = [-1,1,0,0] #상하좌우
    dj = [0,0,-1,1]

    graph = {}
    for i in range(N):
        for j in range(N):
            if miro[i][j] != 1:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<= ni < N and 0<= nj < N and miro[ni][nj] != 1:
                        if (i,j) not in graph:
                            graph[(i,j)] = [(ni,nj)]
                        elif (ni,nj) not in graph[(i,j)]:
                            graph[(i,j)].append((ni,nj))

    ans = BFS(s,e)
    print(f'#{tc} {ans}')