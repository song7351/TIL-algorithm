"""
보드의 크기는 44 66 88중 1개 = N
정가운데 wb/bw 무조건 초기설정
돌은 무조건 백흑백 흑백흑 과같이 사이에 놓을수 있는곳에다가 놓아야한다.(가로세로대각선)
만약 성공시, 사이의 돌은 내것으로 변함.
첫줄: 테스트케이스
2줄: N M 보드크기, 플레이어 돌놓는횟수
게임이 끝난뒤 흑돌/ 백돌 수량 표시.
1은 흑돌 -1는 백돌
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    # 게임판
    board = [[0]*N for _ in range(N)]
    # 기본 게임 세팅
    board[N//2][N//2], board[N//2 - 1][N//2 - 1] = -1,-1
    board[N//2][N//2 - 1], board[N//2 - 1][N//2] = 1,1
    # 12시부터 시계방향 8방위
    di = [-1,-1,0,1,1,1,0,-1]
    dj = [0,1,1,1,0,-1,-1,-1]
    for i in range(M):
        lst = list(map(int,input().split()))         # 주어진 설정은 1부터이기 때문에 -1씩 설정(보드는 0부터로 설정했음)
        x,y,c = lst[0]-1, lst[1]-1, lst[2]           # 색변환의 편의성을 위해서 흑돌은1 백돌은 -1로 설정
        if c == 2:
            c = -1
        board[x][y] = c           # 돌놓고 설정 시작
        for j in range(8):        # 8방위 검사
            tmp = []              # 반대색 저장하는 곳. 추후 한꺼번에 색변환 예정
            ni = x + di[j]
            nj = y + dj[j]
            if 0<= ni < N and 0<= nj < N:
                z = 1                       # 점점더 멀어지게하는 변수
                if board[ni][nj] == -c:     # 만약 반대색이 나왔다면?
                    tmp.append([ni,nj])     # 추후 한꺼번에 색변환을 위해서 저장
                    while True:             # 같은방향으로 계속 검사.
                        ki = ni + di[j]*z
                        kj = nj + dj[j]*z
                        z += 1
                        if 0 <= ki < N and 0 <= kj < N:     # 같은방향으로 검사시,
                            if board[ki][kj] == c:          # 같은 색이 나오면
                                for a,b in tmp:             # 한꺼번에 색변환
                                    board[a][b] = c
                                break                       # 색변환후 break -> 30행 다른 방향검사시작
                            elif board[ki][kj] == 0:        # 빈곳이 나오면?
                                break                       # break
                            else:                           # 반대색이 나오면?
                                tmp.append([ki,kj])         # 추후 한꺼번에 색변환을 위해서 저장
                        else:               # 언제까지? 같은색이 나오거나(43행) 보드판을 벗어날때까지
                            break
    # 흑돌백돌 카운트.
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == -1:
                cnt2 += 1
    print(f'#{tc} {cnt1} {cnt2}')
