"""
N명의 직원
N개의 일
직원들의 번호가 1부터 N
 i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.
 “주어진 일이 모두 성공할 확률”의 최댓값
"""

test_case = int(input())

def f(i,N,col,v,arr):
    global ans
    if i == N:
        if v*100 > ans:
            ans = v*100
    elif v*100 < ans:
        return
    else:
        for j in range(N):
            if j not in arr:
                f(i+1, N, col+1, v*board[col][j], arr+[j])

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    ans = 0
    for i in range(N):
        f(1,N,1,board[0][i], lst+[i])
    ans = round(ans, 6)
    print(f'#{tc} {ans}')