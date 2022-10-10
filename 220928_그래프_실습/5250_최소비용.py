"""
항상 출발은 0,0 도착은 n-1,n-1
기본 이동연료는 1
항상 높은곳으로 이동시 높이 차이만큼 추가 연료 소모
"""

test_case = int(input())

def dfs(x,y,fuel):
    global ans
    if x == N-1 and y == N-1:
        if ans > fuel:
            ans = fuel
    elif fuel > ans:
        return
    else:
        for di,dj in [(1,0),(0,1)]:
            ni = x + di
            nj = y + dj
            if 0<= ni < N and 0<= nj< N:
                diff = 0
                if board[x][y] < board[ni][nj]:
                    diff = board[ni][nj]
                dfs(ni,nj,fuel+1+diff)

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 1000*100*100
    dfs(0,0,board[0][0])

    print(f'#{tc} {ans}')