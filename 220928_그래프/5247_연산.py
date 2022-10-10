"""
1~100만
"""
test_case = int(input())

def bfs():
    while arr:
        n, cnt = arr.pop(0)
        if n == M:
            print(cnt)
            return
        if 1<= n+1 <= 1000000 and visited[n+1] == 0:
            visited[n+1] = 1
            arr.append((n+1, cnt+1))
        if 1<= n-1 <= 1000000 and visited[n-1] == 0:
            visited[n-1] = 1
            arr.append((n-1,cnt+1))
        if 1<= 2*n <= 1000000 and visited[2*n] == 0:
            visited[2*n] = 1
            arr.append((2*n, cnt+1))
        if 1<= n-10 <= 1000000 and visited[n-10] == 0:
            visited[n-10] = 1
            arr.append((n-10, cnt+1))

for tc in range(1, test_case + 1):
    N,M = map(int, input().split())
    visited = [0]*1000001
    arr = [(N,0)]
    visited[N] = 1
    print(f'#{tc}', end=' ')
    bfs()