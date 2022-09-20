import sys; sys.stdin = open('1242_암호스캔.txt')

pat = {211: 0, 221: 1, 122: 2, 411: 3, 132: 4,
       231: 5, 114: 6, 312: 7, 213: 8, 112: 9}


def erase(p, q, r):
    h = 0
    while arrb[p + h][q] == 1:
        h += 1
    for i in range(p, p + h):
        for j in range(q - r * 56 + 1, q + 1):
            arrb[i][j] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    if tc != 9:
        continue
    arrb = [[0] * (M * 4) for _ in range(N)]
    # 16진수 -> 2진수 형태로 변환
    for i in range(N):
        for j in range(M):
            h = int(arr[i][j], 16)  # 16진수 문자열 -> 정수
            for k in range(4):
                if h & (1 << (3 - k)):  # [0] ~[3] -> b3 ~ b0
                    arrb[i][j * 4 + k] = 1
                else:
                    arrb[i][j * 4 + k] = 0

    ans = 0
    M *= 4
    for i in range(N):
        # for j in range(M-55):   # 1/0이 56개는 남아있어야 함
        j = 0
        k = 0
        while j < M - 55:
            code = [0] * 8

            for k in range(8):
                a, b, c = 0, 0, 0
                while j < M and arrb[i][j] == 0:
                    j += 1
                if j == M:
                    break
                while arrb[i][j] == 1:
                    j += 1
                    a += 1
                while arrb[i][j] == 0:
                    j += 1
                    b += 1
                while arrb[i][j] == 1:
                    j += 1
                    c += 1
                r = min(a, b, c)
                code[k] = pat[a // r * 100 + b // r * 10 + c // r]
            else:
                check = (code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]
                print(code)
                if check % 10 == 0:
                    ans += sum(code)
                erase(i, j - 1, r)
                k = 0
    print(f'#{tc} {ans}')