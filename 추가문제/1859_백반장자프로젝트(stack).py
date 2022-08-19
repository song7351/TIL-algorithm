test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    market = list(map(int, input().split()))
    ans = 0
    max_num = market.pop()                  # 가장 뒤부터 비교한다.
    while len(market) != 0:
        if market[-1] < max_num:            # max_num보다 작다면 사고팔아서 수익처리하고 pop
            ans += max_num - market[-1]
            market.pop()
        else:
            max_num = market.pop()          # max_num보다 크다면 max_num변경

    print(f'#{tc} {ans}')