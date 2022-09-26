test_case = int(input())

def f(i,N,arr):
    if i == N:
        pass
    else:
        for j in range((N**2)-1):
            for k in range(i+1,N):
                f(i+1,N)

for tc in range(1, test_case + 1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    lst = [[0]*(N**2)]
    tmp = 0
    grp = []
    for i in range(N):
        for j in range(N):
           lst[tmp] = (i,j)
           tmp += 1
    f(0,N,grp)