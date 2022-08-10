'''
## 모든 원소의 합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#
s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]
print(s)
'''

## 각 행의 합을 구하고 그 중 최대값을 출력하시오
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#
max_s = 0           # 최대 행의 합
for i in range(N):
    s = 0           # 행의 합
    for j in range(N):
        s += arr[i][j]
    if s > max_s:
        max_s = s
print(max_s)
