N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#
s = [0] * ( 2 * N - 1)
for i in range(N):
    for j in range(N):
        s[i+j] += arr[i][j]

print(s)