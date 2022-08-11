'''
숫자 1은 0, 0은 1로 바뀌는 연산을 토글 이라고 한다.

각 칸이 1 또는 0으로 초기화된 N x N 영역이 주어진다. 3<=N<=20

각 칸의 숫자는 M초까지 1초마다 다음의 조건에 따라 토글된다. 1<=M<=100

    (1) 각 영역은 i행과 j열로 구분된다. 1 <= i, j <= N
    (2) k초가 되는 순간, i + j가 k와 같거나 k의 배수가 되는 영역은 토글된다. 1 <= k <= M
    (3) 단, M이 k의 배수인 경우와 M초에는 (2)를 따르는 대신 전체가 토글 된다.

M초후 1인 영역의 개수를 출력하시오.
'''
test_case = int(input())

for tc in range(1, test_case+1):
    N,M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    k = 0   #초
    while k < M:
        k += 1
        for i in range(N):
            for j in range(N):
                #단, M이 k의 배수인 경우와 M초에는 (2)를 따르는 대신 전체가 토글 된다.
                if (M % k == 0) or (k == M):
                    if board[i][j] == 1:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
                # (2) k초가 되는 순간, i + j가 k와 같거나 k의 배수가 되는 영역은 토글된다.
                # i와 j는 1부터 계산하므로 각각 +1
                elif ((i+j+2) == k) or (i+j+2) % k == 0:
                    if board[i][j] == 1:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1
    
    print(f'#{tc} {cnt}')