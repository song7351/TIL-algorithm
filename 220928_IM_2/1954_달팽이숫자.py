test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    num = 2
    i,j = 0,0
    board[0][0] = 1
    d = 0
    for _ in range(N**2-1):
        while True:
            ni = i + di[d]
            nj = j + dj[d]
            if 0<= ni <N and 0<= nj <N and board[ni][nj] == 0:
                i,j = ni,nj
                board[i][j] = num
                num += 1
                break
            else:
                d = (d+1)%4
    print(f'#{tc} ')
    for i in range(N):
        print(*board[i])