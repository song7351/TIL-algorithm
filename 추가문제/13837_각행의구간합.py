"""
2차원 리스트 : 크기는 N
각 행에서 길이가 K인 구간의 합을 구한다.
예시
크기가 5인 리스트
0행: 0~2
1행: 1~3
2행: 2~4
3행: 3~4
4행: 4
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for i in range(N):
        num_sum = 0
        for k in range(K):
            nj = i + 1*k                # 모든 구간은 board[i][i]부터 시작한다.
            if 0<=nj < N:
                num_sum += board[i][nj]
        if num_sum > max_sum:
            max_sum = num_sum

    print(f'#{tc} {max_sum}')