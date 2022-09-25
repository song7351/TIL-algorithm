"""
 N은 4 이상 20 이하
"""
test_case = int(input())

def f(i,j,arr):
    global ans,N
    lst = []
    cnt = 0
    for d in range(4):  # 방향설정
        cnt = arr[d]
        while cnt:
            cnt -= 1
            ni = i + di[d]
            nj = j + dj[d]
            if 0<= ni < N and 0<= nj< N:
                i,j = ni,nj
                lst.append(board[i][j])
            else:
                return
    if len(set(lst)) == arr[4]:
        ans = arr[4]

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    move = []
    for i in range(1,N):
        for j in range(1,N):
            move.append([i,j,i,j,2*(i+j)])  # 우하단 좌하단 좌상단, 우상단이동 횟수,합

    move.sort(key=lambda x: -x[4])  # 이동횟수가 가장 많은것부터 검사시작

    di = [1,1,-1,-1]
    dj = [1,-1,-1,1]
    ans = -1
    for i in range(N):
        for j in range(N):
            for k in move:
                if k[4] > ans:
                    f(i,j,k)

    print(f'#{tc} {ans}')