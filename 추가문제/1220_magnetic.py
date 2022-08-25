"""
파란색은 N극에
빨간색은 S극에 이끌린다.
그 다음 줄부터 100 x 100크기의 테이블의 초기 모습이 주어진다.
1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며
테이블의 윗부분에 N극이 아래부분에 S극이 위치한다고 가정한다.
-> 1은 아래로 떨어지려하고 2는 위로 올라가려한다.
"""
"""

"""
test_case = 10

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    ans = 0

    for i in range(N):
        s = 99
        e = 0
        # 어쩌든 각 세로줄에 가장 윗부분은 1이고 가장 밑부분은 2이다.
        for j in range(N):
            if board[j][i] == 1:
                s = j
                break
        for j in range(N-1, -1, -1):
            if board[j][i] == 2:
                e = j
                break
        # 만약 가장 밑부분이 가장 윗부분보다 높다면 0이다.
        if e < s:
            continue
        check_list = []
        for j in range(s, e+1):                 # 해당 부분중 0이 아닌값으로 리스트 생성
            if board[j][i] != 0:
                check_list.append(board[j][i])

        for j in range(len(check_list)-1):      # 리스트중 12로 연속된 부분이 교착상태.
            if check_list[j] == 1 and check_list[j+1] == 2:
                ans += 1

    print(f'#{tc} {ans}')