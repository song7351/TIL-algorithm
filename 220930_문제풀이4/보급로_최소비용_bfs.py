"""
최소비용 문제
"""
test_case = int(input())

def bfs():
    waited = [(0,0)]
    while waited:
        x,y = waited.pop(0)
        c = cost[x][y]
        for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
            ni = x + di
            nj = y + dj
            if 0<= ni < N and 0<= nj < N:
                c2 = c + board[ni][nj]
                if c2 < cost[ni][nj]:
                    cost[ni][nj] = c2
                    waited.append((ni,nj))

INF = int(1e9)
for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    cost = [[INF]*N for _ in range(N)]
    #print(board)
    cost[0][0] = board[0][0]
    bfs()
    #print(cost)
    print(f'#{tc} {cost[N-1][N-1]}')