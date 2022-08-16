"""
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

팰린드롬!
"""
def palindrome(arr, target):
    #가로 검사.
    for i in range(len(arr)):
        left = 0
        right = left + target - 1
        for j in range(len(arr)-target+1):
            row_word = arr[i][left:right+1]
            rr_word = row_word[::-1]
            if row_word == rr_word:
                return row_word
            else:
                left += 1
                right += +1
    return 0

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    ans = palindrome(board, M)
    if ans != 0:
        print(f'#{tc} {"".join(ans)}')
    else:
        # 가로세로를 뒤집어준다.
        new_board = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_board[i][j] = board[j][i]

        ans = palindrome(new_board,M)
        print(f'#{tc} {"".join(ans)}')
