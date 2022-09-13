"""
크기 : N
한줄에 1개씩 숫자를 골랐을때 최소합을 구해라
단, 고른 숫자의 세로열에서는 고를 수 없다.
"""
def sunyeol(i, n):
    global min_sum
    if i == n:
        sum_ans = 0
        for j in range(N):
            sum_ans += board[j][col_list[j]]    # 각 row마다 순열로 확인할 인덱스 반영
        if sum_ans < min_sum:
            min_sum = sum_ans
    else:
        for j in range(i, n):
            col_list[i], col_list[j] = col_list[j], col_list[i]
            sunyeol(i+1, n)
            col_list[i], col_list[j] = col_list[j], col_list[i]

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    col_list = [ i for i in range(N)] # 순열로 확인할 인덱스를 리스트로 생성.
    board = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 0
    for i in range(N):
        min_sum += board[i][i]

    sunyeol(0, N)

    print(f'#{tc} {min_sum}')
