'''
크기가 NxN인 배열의 부분 배열인  nxm 배열 원소의 합 중 가장 큰 값을 출력하시오.
다음은 N=5, n=2, m=3일 때 오른쪽 아래의  부분 배열 영역을 나타낸다. 
첫 줄에 테스트케이스개수 T가 주어지고, 다음 줄 부터 각 테스트 케이스 별로 N, n, m이 주어진다. 이후 N개의 줄 각각 N개의 1 또는 0이 주어진다.
10<=N<=100, 1<=n, m
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N, n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0
    #검색할 인덱스 범위 설정(시작점)
    for i in range(N-n+1):
        for j in range(N-m+1):
            sum = 0
            #시작점으로부터 가로세로 n,m만큼 요소 합산
            for k in range(n):
                for l in range(m):
                    sum += board[i+k][j+l]
            if sum > max_sum:
                max_sum = sum
    print(f'#{tc} {max_sum}')