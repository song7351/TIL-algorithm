"""
N 크기 농장 (N은 항상 홀수)

"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    mid = N // 2
    ans = 0

    # 중간값 까진 중간값 인덱스에서 좌우로 1,2,3... 커짐
    # 중간값 이후로는 인덱스에서 좌우로 3,2,1... 작아짐
    for i in range(N):
        if i <= mid:
            for j in range(mid-i, mid+i+1):
                ans += board[i][j]
        else:
            for j in range(mid-(N-1-i),mid+1+(N-1-i)):
                ans += board[i][j]

    print(f'#{tc} {ans}')