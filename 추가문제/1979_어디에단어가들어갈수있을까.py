'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.
'''

test_case = int(input())

for tc in range(1, test_case + 1):
    N, K = int(input().split())
    board = [ list(map(int, input())) for _ in range(N) ]
    check = []
    for i in range(N-1):
        r_cnt = 1
        c_cnt = 1
        for j in range(N-1):
            if board[i][j] == 1 and board[i][j+1] == 1:
                r_cnt += 1
            elif board[i][j] == 1 and board[i][j+1] == 0 and r_cnt == K:
                    check.append(r_cnt)
                    r_cnt = 1
            if board[j][i] == 1 and board[j+1][i] == 1:
                c_cnt += 1
            elif board[j][i] == 1 and board[j][i+1] == 0 and c_cnt == K:
                    check.append(c_cnt)
                    c_cnt = 1

    cnt = 0
    for i in check:
        if i == K:
            cnt += 1
    print(f'#{tc} {cnt}')