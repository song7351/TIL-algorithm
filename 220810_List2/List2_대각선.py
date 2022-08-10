## 우하향 대각선의 합
#
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#
s = 0
for i in range(N):
    s += arr[i][i]
print(s)
#
## 좌하향 대각선의 합
s2 = 0
for i in range(N):
    s2 += arr[i][N-1-i]
print(s2)
#
## x 대각선 합?
s3 = 0
for i in range(N):
    s3 += arr[i][i]
    s3 += arr[i][N-1-i]
    if i == (N // 2):
        s3 -= arr[i][i]
print(s3)