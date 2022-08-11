'''
파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N,M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # 십자모드
    di = [1,-1,0,0] #상하좌우
    dj = [0,0,-1,1]
    # X모드
    xi = [1,1,-1,-1]    #왼위 오위 오아 왼아
    xj = [-1,1,1,-1]
    
    max_sum = 0
    for i in range(N):
        for j in range(N):
            d_sum = board[i][j]
            x_sum = board[i][j]
            for k in range(1,M):
                for l in range(4):
                    ni = i + di[l]*k
                    nj = j + dj[l]*k
                    mi = i + xi[l]*k
                    mj = j + xj[l]*k
                    if 0<= ni< N and 0<= nj < N:
                        d_sum += board[ni][nj]
                    if 0<= mi< N and 0<= mj < N:
                        x_sum += board[mi][mj]
                        
            if d_sum >= x_sum:
                ans_sum = d_sum
            else:
                ans_sum = x_sum
                
            if ans_sum > max_sum:
                max_sum = ans_sum
            
    print(f'#{tc} {max_sum}')