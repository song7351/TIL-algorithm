def f(i, N):
    global minV
    if i == N:
        s = 0
        for k in range(N):
            s += arr[k][P[k]]
        if s < minV:
            minV = s
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]

def f2(i,s,N):  # i행, s i-1행까지의합, N은 총행수
    global minV
    if i == N:
        s = 0
        for k in range(N):
            s += arr[k][P[k]]
        if s < minV:
            minV = s
    elif minV <= s:
        return
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, s+arr[i][P[i]], N)
            P[i], P[j] = P[j], P[i]

test_case = 10
for tc in range(1, test_case+1):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    minV = 1000

    #f(0,N)
    f(0,0,N)
    print(f"#{tc}")