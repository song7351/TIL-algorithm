"""
 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다.
 0~9: 모든 수는 1로 끝남. 그러므로 뒤에서부터 검색해서 1이 나오면,
 앞으로 55칸을 가야된다.
"""
import sys; sys.stdin = open('1240_단순2진암호코드.txt')

def f():
    for k in range(N):
        for l in range(M-1,-1,-1):
            if board[k][l] == 1:
                return k,l

test_case = int(input())
code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
for tc in range(1, test_case + 1):
    N, M = map(int,input().split())
    board = [list(map(int, input())) for _ in range(N)]

    x,y = f()
    for i in range(8):
        y -= 7
    y += 1

    secret_code = []
    for i in range(8):
        secret_code.append(code.get(''.join(map(str, board[x][y:y+7]))))
        y += 7

    verifi_code = (secret_code[0] + secret_code[2] + secret_code[4] + secret_code[6]) * 3 \
                + (secret_code[1] + secret_code[3] + secret_code[5] + secret_code[7])

    ans = 0
    if not verifi_code % 10:
        ans = sum(secret_code)

    print(f'#{tc} {ans}')