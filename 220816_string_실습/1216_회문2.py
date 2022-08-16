"""
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

글자 판은 무조건 정사각형으로 주어진다.

ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

총 10개의 테스트케이스가 주어진다.
"""
def palindrome(arr):
    max_cnt = 0
    for i in range(100):
        cnt = 0
        for j in range(100):
            for k in range(99, j-1, -1):
                if arr[i][j] == arr[i][k]:
                    word = arr[i][j:k+1]
                    r_word = word[::-1]
                    if word == r_word:
                        cnt = k-j+1
                        break
            if cnt > max_cnt:
                max_cnt = cnt

    return max_cnt


test_case = 10

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(input()) for _ in range(100)]


    ans1 = palindrome(board)

    for i in range(100):
        for j in range(100):
            board[i][j] = board[j][i]

    ans2 = palindrome(board)

    if ans2 > ans1:
        ans = ans2
    else:
        ans = ans1
    print(f'#{tc} {ans} {ans2} {ans1}')