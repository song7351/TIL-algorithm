test_case = int(input())
di = [-1,1,1,-1]
dj = [1,1,-1,-1]


def check(x,y):
    L = 1
    cnt = 4
    while cnt:
        cnt = 4
        for k in range(4):
            ni = x + di[k] * L
            nj = y + dj[k] * L
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 1:
                    return False
            else:
                cnt -= 1
        L += 1
    return True


def f(i,N,col,arr):
    global ans
    if i == N:
        ans += 1
    else:
        for j in range(N):                  # 세로열 설정
            if j not in arr:                # 만약 세로열이 겹치지 않는다면,
                if check(col,j):            # 확인해라.
                    board[col][j] = 1
                    f(i+1,N,col+1,arr+[j])
                    board[col][j] = 0


for tc in range(1, test_case + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    lst = []                    #세로열 저장리스트
    ans = 0
    for i in range(N):          # 모든 가로열에 퀸은 한개씩만 들어간다.
        board[0][i] = 1
        f(1, N, 1, lst+[i])
        board[0][i] = 0
    print(f"#{tc} {ans}")