"""
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우, N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

"""
"""
다른문제 풀이
1. 어차피 파스칼의 삼각형의 크기가 최대 10이라면, 그냥 10짜리를 만든다.
2. 그리고 N을 입력 받을때마다, 출력만 돌리면 된다.

"""
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    # 전체 사이즈의 보드판을 만든다.
    board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            # 시작값(인덱스0)은 무조건 1로 시작한다.
            if j == 0:
                board[i][j] = 1
            # 현재 위치의 값은 이전줄의 이전idx와 현재idx값의 합이다.
            else:
                board[i][j] = board[i-1][j-1] + board[i-1][j]

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            # 값들중 0이 아닌 값만 출력한다.
            if board[i][j] != 0:
                print(board[i][j], end=" ")
        print()



