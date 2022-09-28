"""
N종의 제품을 N곳의 공장
한 행과 한 열에 하나만 사용한다.
"""
test_case = int(input())

def f(i,N,col,s,arr):
    global ans
    if i == N:
        if s < ans:
            ans = s
    elif s > ans:
        return
    else:
        for j in range(N):
            if j not in arr:
                f(i+1, N, col+1, s+board[col+1][j], arr + [j])

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    ans = 1500
    for i in range(N):
        f(1,N,0, board[0][i],lst+[i])
    print(f'#{tc} {ans}')
