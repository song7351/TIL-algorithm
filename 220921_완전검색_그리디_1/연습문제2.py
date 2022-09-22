"""
6자리 숫자에 대해서 완전 검색을 적용하여 baby-gin을 검사하세요.
baby-gin이란?
0~9가 적힌 카드중 6장을 받는다.
승리조건
1. 런: 3장의 카드가 연속적인 번호. 단 901은 제외
2. 트리플: 같은 번호를 가지는 3장의 카드

입력
124783
667767
053060
101123
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N = list(map(int, input()))
    board = [0] * 10
    for i in N:
        board[i] += 1

    ans = 'Lose'
    triple = 0
    run_a = 0
    cnt = 0                 # 연속되는 수를 파악하는 용도
    for i in range(10):
        if board[i] == 6:   # 같은 수가 6개 사용되면 트리플이 2개
            triple = 2
        elif board[i] >= 3: # 1개의 수가 3개이상 사용되면 트리플이 1개
            triple += 1

        if board[i] == 0:
            cnt = 0
        else:
            cnt += 1        # 0이 아니면 해당 인덱스의 카드를 가지고있다.

        if cnt == 3:        # 연속된 카드가 3장이라면, run
            run_a += 1
            cnt = 0

    if run_a+triple == 2:   # 런과 트리플의 수를 합쳐서 2개면 baby gin
        ans = "Baby Gin"

    print(f'#{tc} {ans}')