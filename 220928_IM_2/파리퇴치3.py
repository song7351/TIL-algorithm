test_case = int(input())

di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

def spray(i,j,M):
    global ans

    plus = board[i][j]
    cross = board[i][j]
    for L in range(1,M+1):
        for k in range(8):
            ni = i + di[k]*L
            nj = j + dj[k]*L
            if 0<= ni < N and 0<= nj < N:
                if k % 2:  # 홀수 = x자
                    cross += board[ni][nj]
                else:
                    plus += board[ni][nj]

    if cross > ans:
        ans = cross
    if plus > ans:
        ans = plus


for tc in range(1, test_case + 1):
    N,M = map(int,input().split())
    board= [list(map(int,input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        for j in range(N):
            spray(i,j,M-1)

    print(f'#{tc} {ans}')