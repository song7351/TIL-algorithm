'''
상하좌우 이웃원소의 합을 구해라

'''

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0] #상하좌우
    dj = [0, 0, -1, 1]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<= ni < N and 0<= nj < N:
                    sum += board[ni][nj]
            if sum > max_sum:
                max_sum = sum
    
    print(f'#{tc} {max_sum}')