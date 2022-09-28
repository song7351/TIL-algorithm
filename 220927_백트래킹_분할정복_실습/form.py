test_case = int(input())

def f(i,N,col,v,arr):
    global ans

    if i == N:
        if v/bunmo > ans:
            ans = v/bunmo
    elif v/bunmo < ans:
        return
    else:
        for j in range(N):
            if j not in arr:
                f(i+1, N, col+1, v*board[col+1][j], lst+[j])

for tc in range(1, test_case + 1):
    N = int(input())
    bunmo = 100**(N-1)
    board = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    ans = 0
    for i in range(N):
        f(0,N-1,1,board[0][i], lst+[i])
    print(f'#{tc} {ans}')