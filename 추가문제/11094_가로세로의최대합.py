'''
N x N 배열에서 한 칸을 선택했을 때 그 칸을 포함하는 가로 행과 세로 열에 포함된 값들의 총합이 최대가 되는 경우를 찾고 싶다.
한지점에서 본인을 포함한 십자의 합 구하는 문제
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    di = [-1,1,0,0] #상하좌우
    dj = [0,0,-1,1]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            sum = board[i][j]
            #십자 행과 열 덧셈
            for k in range(1,N):
                for l in range(4):
                    ni = i + di[l]*k
                    nj = j + dj[l]*k
                    if 0<= ni < N and 0<= nj < N:
                        sum += board[ni][nj]
            if sum > max_sum:
                max_sum = sum
            
    print(f'#{tc} {max_sum}')