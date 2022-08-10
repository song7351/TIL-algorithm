## 우하향 대각선기준으로 왼쪽/ 오른쪽 영역(합) 값
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 우하향(1)
right_sum = 0
left_sum = 0
for i in range(N):
    for j in range(N):
        if i < j:
            right_sum += arr[i][j]
        elif i > j:
            left_sum += arr[i][j]
print(left_sum,right_sum)
#
## 우하향(2)
s1 = 0
s2 = 0
for i in range(N):
    for j in range(i+1, N):
        s2 += arr[i][j]
        s1 += arr[j][i]
print(s1, s2)
#