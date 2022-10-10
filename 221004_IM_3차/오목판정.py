"""
8방향 검사할 필요는 없다.
하려면 하는데 걍 그 절반인 4방향만 해도 동일한 결과.
"""
test_case = int(input())

def check(i,j):
    for di,dj in [(-1,1),(0,1),(1,0),(-1,-1)]:
        k = 1
        cnt = 1
        while k < 5:
            ni = i + di*k
            nj = j + dj*k
            k += 1
            if 0<= ni < N and 0<= nj < N:
                if board[ni][nj] == 'o':
                    cnt += 1
                else:
                    break
            else:
                break
        if cnt == 5:
            return True
    else:
        return False

def search():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                if check(i,j):
                    print('YES')
                    return
    else:
        print('NO')
        return

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    print(f'#{tc}', end=' ')
    search()