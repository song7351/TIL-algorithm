'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
'''

for tc in range(1,10+1):     # 총 10번의 테스트
    max_ans = 0 
    right_diagonal = 0
    left_diagonal = 0
    N = int(input())
    num_board = [list(map(int, input().split())) for _ in range(100)]
    
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            if i == j:                                  #우하향 대각선 조건
                right_diagonal += num_board[i][j]
                if max_ans < right_diagonal:
                    max_ans = right_diagonal
            if i + j == 9:                              #좌하향 대각선 조건
                left_diagonal += num_board[i][j]
                if max_ans < left_diagonal:
                    max_ans = left_diagonal
            row_sum += num_board[i][j]                  #가로행 합
            col_sum += num_board[j][i]                  #세로열 합
        if max_ans < row_sum:
            max_ans = row_sum
        if max_ans < col_sum:
            max_ans = col_sum

    print(f"#{tc} {max_ans}")