'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        cnt = 0
        #각 범위별 color값을 합친다.
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                board[i][j] += color
        
        #중복되면 최소값이 3
        for i in range(10):
            for j in range(10):
                if board[i][j] >= 3:
                    cnt += 1
        
    print(f'#{tc} {cnt}')