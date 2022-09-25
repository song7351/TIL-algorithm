"""
4×4 크기의 격자판이 있다.
격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.
시작 + 6번이동 -> 총 7자리 숫자
"""
test_case = int(input())

def f(i,j,word):
    if len(word) == 7:
        lst.append(word)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni<4 and 0<= nj<4:
                f(ni,nj,word+board[ni][nj])

for tc in range(1, test_case + 1):
    board = [list(input().split()) for _ in range(4)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    lst = []
    for i in range(4):
        for j in range(4):
            f(i,j,board[i][j])
    lst = set(lst)
    print(f'#{tc} {len(lst)}')