test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N) ]

    print(f'#{tc}')