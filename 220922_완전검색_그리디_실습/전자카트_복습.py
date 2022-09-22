test_case = int(input())

def f(i, c, s):
    global ans
    if c == len(board)-1:
        s += board[i][0]
        if s < ans:
            ans = s
    elif s > ans:
        return
    else:
        for j in range(1,len(board)):
            if used[j] == 0:
                used[j] = 1
                f(j,c+1,s+board[i][j])
                used[j] = 0

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    used = [0]*N
    ans = 1000
    #시작지점, 이동횟수, 합
    f(0,0,0)
    print(f'#{tc} {ans}')