"""
크기가 NxN인 2차원 배열 내부에 1로 채워진 사각 영역이 있다. 사각형의 가로 세로 칸수를 곱한 값을 출력하는 프로그램을 만드시오. 사각형이 여러 개인 경우 곱이 가장 큰 경우를 출력한다.
다음은 N=10인 2차원 배열의 예로, 곱은 12가 된다.
"""
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N) ]

    #방향판 - 우, 하
    di = [0, 1]
    dj = [1, 0]
    max_area = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                row = 1
                col = 1
                x,y = i,j
                #가로길이 구하기.
                ni, nj = x,y
                while board[ni][nj] >= 1:
                    nj = j + dj[0]
                    if 0<= ni < N and 0<=nj <N and board[ni][nj] == 1:
                        j = nj
                        row += 1
                #세로길이 구하기
                ni, nj = x, y
                while board[ni][nj] >= 1:
                    ni = i + di[1]
                    if 0<= ni < N and 0<=nj <N and board[ni][nj] == 1:
                        i = ni
                        col += 1

                area = row * col
                if area > max_area:
                    max_area = area

    print(f'#{tc} {max_area}')