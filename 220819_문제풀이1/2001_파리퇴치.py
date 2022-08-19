"""
보드판 = N * N
파리채 = M * M

1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
"""

test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())    # N: 보드크기, M: 파리채크기
    board = [list(map(int, input().split())) for _ in range(N)]

    max_pali = 0
    for i in range(N-M+1):              # 검색할 최대범위는 보드크기-파리채크기
        for j in range(N-M+1):
            pali = 0
            for k in range(M):          # 파리채 범위만큼 합산.
                for l in range(M):
                    pali += board[i+k][j+l]
            if pali > max_pali:
                max_pali = pali

    print(f"#{tc} {max_pali}")