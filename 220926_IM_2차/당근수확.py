"""

"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = list(map(int, input().split()))
    a,b = 0,0
    diff = 200
    for i in range(1,N-1):
        if abs(sum(board[:i]) - sum(board[i:])) < diff:
            diff = abs(sum(board[:i]) - sum(board[i:]))
            a = i

    print(f'#{tc} {a} {diff}')