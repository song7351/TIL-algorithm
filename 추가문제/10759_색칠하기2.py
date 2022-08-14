'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다. N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 빨간색 영역과 파란색 영역의 외곽 길이를 구하는 프로그램을 만드시오. 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
'''
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]

    #보드 만들기
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        # 각 범위별 color값을 합친다.
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] += color

    #방향판 - 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    cnt = 0
    for i in range(10):
        for j in range(10):
            if (board[i][j] == 1) or (board[i][j] == 2):
                side = 4
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 우선 유효 범위 안에 들어있는지?
                    if 0<= ni < 10 and 0<= nj < 10:
                        #만약 근처 값이 같은색이라면 변이 삭제됨. 다른 색은 상관없음.
                        if board[ni][nj] == board[i][j]:
                            side -= 1
                cnt += side

    print(f'#{tc} {cnt}')