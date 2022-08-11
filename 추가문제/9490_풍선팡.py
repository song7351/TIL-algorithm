'''
종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고, 어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.

예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    di = [-1,1,0,0] #상하좌우
    dj = [0,0,-1,1]
    
    for i in range(N):
        for j in range(M):
            sum = board[i][j]
            x = board[i][j] #터트린 숫자만큼 가로세로 추가 터짐
            for k in range(1,x+1):
                for l in range(4):      #상하좌우 반복
                    ni = i + di[l]*k
                    nj = j + dj[l]*k
                    if 0<= ni <N and 0<= nj< M:
                        sum += board[ni][nj]
            if sum > max_num:
                max_num = sum

    print(f'#{tc} {max_num}')