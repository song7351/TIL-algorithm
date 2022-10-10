"""
항상 출발은 0,0 도착은 n-1,n-1
기본 이동연료는 1
항상 높은곳으로 이동시 높이 차이만큼 추가 연료 소모
"""
test_case = int(input())

def bfs():
    waited = [(0,0)]
    while waited:
        x,y = waited.pop(0)
        fuel = cost[x][y]
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            ni = x + di
            nj = y + dj
            if 0<= ni < N and 0<= nj < N:
                # 연료 계산
                diff = 0
                if board[x][y] < board[ni][nj]:
                    diff = board[ni][nj] - board[x][y]
                fuel2 = fuel+1+diff

                # 연료값이 작거나 처음에는 값을 설정한.
                if fuel2 < cost[ni][nj] or cost[ni][nj] == 0:
                    cost[ni][nj] = fuel2
                    waited.append((ni,nj))



for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0] * N for _ in range(N)]
    bfs()
    print(f'#{tc} {cost[N-1][N-1]}')