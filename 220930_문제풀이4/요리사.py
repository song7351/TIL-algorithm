"""
2개의 요리가 최소차이가 발생해야한다.
(x)최소신장_kruskal처럼 접근해서 짝/홀 번갈아 선택하면 안되나...?
그러면 걍 2//N 개씩 만드는 조합을 구해서 직접 다 더한다?
"""
test_case = int(input())

def nCr(n,r,s):
    if r == 0:
        tmp = comb[:]
        tmp_jaelyo.append(tmp)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = jaelyo[i]
            nCr(n,r-1,i+1)

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    jaelyo = [i for i in range(N)]
    #print(jaelyo)

    tmp_jaelyo = []
    r = N//2
    comb = [0] * r
    nCr(N, r, 0)
    #print(tmp_jaelyo)
    #print(A)
    #print(B)
    minV = int(1e9)
    for i in range(len(tmp_jaelyo)):
        sum_a = 0
        sum_b = 0
        A = tmp_jaelyo[i]
        B = list(set(jaelyo) - set(tmp_jaelyo[i]))
        for j in range(N//2 - 1):
            for k in range(j+1,N//2):
                sum_a += board[A[j]][A[k]]
                sum_a += board[A[k]][A[j]]
                sum_b += board[B[j]][B[k]]
                sum_b += board[B[k]][B[j]]

        if abs(sum_b - sum_a) < minV:
            minV = abs(sum_b - sum_a)

    print(f'#{tc} {minV}')
