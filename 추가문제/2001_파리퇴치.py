'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다
'''
test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0
    #검색할 인덱스 범위 설정(시작점)
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            #시작점으로부터 가로세로 M만큼 요소 합산
            for k in range(M):
                for l in range(M):
                    sum += board[i+k][j+l]
            if sum > max_sum:
                max_sum = sum
    print(f'#{tc} {max_sum}')