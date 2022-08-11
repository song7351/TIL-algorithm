'''
크기가 NxN인 2차원 배열 내부에 1로 채워진 사각 영역이 있다. 사각형의 가로 세로 칸수를 곱한 값을 출력하는 프로그램을 만드시오. 사각형이 여러 개인 경우 곱이 가장 큰 경우를 출력한다.
다음은 N=10인 2차원 배열의 예로, 곱은 12가 된다.
'''
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    box = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                pass
    print(f'#{tc} {board}')