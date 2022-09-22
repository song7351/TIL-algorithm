"""
오른쪽이나 아래로만 이동가능
"""
test_case = int(input())

def find(i,j,s):    #좌표i,j // 진행 합
    global N,ans
    if i == N-1 == j:
        s += board[N-1][N-1]
        if s < ans:
            ans = s
    elif s >= ans:
        return 
    else:
        for di, dj in [(1,0),(0,1)]:
            ni = i + di
            nj = j + dj
            if 0<= ni < N and 0<= nj < N:
                find(ni,nj,s+board[i][j])

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    i,j = 0,0
    ans = 1440
    find(i,j,0)
    print(f'#{tc} {ans}')