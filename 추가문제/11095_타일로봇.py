'''
로봇을 이용해 10x10 크기의 격자로 구분된 벽에 타일을 붙이려고 한다. 
로봇에 대한 명령은 4개의 숫자로 이뤄지며, 사각형으로 이뤄진 작업 영역의 왼쪽 위 모서리 행, 열, 오른 쪽 아래 모서리의 행, 열을 나타낸다. 작업 영역이 중복되는 경우에는 타일이 이미 붙어있는 자리는 제외하고 나머지 칸에 대해 타일을 붙이게 된다. 
N개의 명령이 주어질 때, 실제로 타일이 붙여진 칸의 수를 출력하시오.
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [[0]*10 for i in range(10)]
    for _ in range(N):
        x1,y1,x2,y2 = map(int,input().split())
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                board[i][j] += 1

        cnt = 0
        for i in range(10):
            for j in range(10):
                if board[i][j] >= 1:
                    cnt += 1
    
    print(f'#{tc} {cnt}')