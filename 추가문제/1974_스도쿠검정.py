'''
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.
'''

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(9)]

    ans = [1] * 9
    row_check = [0] * 9
    col_check = [0] * 9
    box_check = [0] * 9
    result = 1
    for i in range(9):
        for j in range(9):
            row_check[board[i][j] - 1] += 1
            col_check[board[j][i] - 1] += 1
        if row_check != ans or col_check != ans:
            result += 1
            break
        else:
            row_check = [0] * 9
            col_check = [0] * 9

    # 검색할 인덱스 범위 설정(시작점)
    for i in [0,3,6]:
        for j in [0,3,6]:
            # 3 * 3
            for k in range(3):
                for l in range(3):
                    box_check[board[i + k][j + l]] += 1
            if box_check != ans:
                result += 1
                break
            else:
                box_check = [0] * 9
    if result != 1:
        result = 0
    print(f'#{tc} {result}')