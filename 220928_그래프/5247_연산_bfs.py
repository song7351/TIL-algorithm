"""
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만드려고한다.
사용할 수 있는 연산이 +1, -1, *2, -10
최소 몇 번의 연산?
"""
test_case = int(input())

def bfs():
    while waited:
        n, cnt = waited.pop(0)
        if n == M:
            print(cnt)
            return
        for i in range(4):
            if i == 0:
                if 1<= n+1 <= 1000000 and visited[n+1] == 0:
                    visited[n+1] = 1
                    waited.append((n+1, cnt+1))
            if i == 1:
                if 1<= n-1 <= 1000000 and visited[n-1] == 0:
                    visited[n-1] = 1
                    waited.append((n-1, cnt+1))
            if i == 2:
                if 1<= n*2 <= 1000000 and visited[n*2] == 0:
                    visited[n*2] = 1
                    waited.append((n*2, cnt+1))
            if i == 3:
                if 1<= n-10 <= 1000000 and visited[n-10] == 0:
                    visited[n-10] = 1
                    waited.append((n-10, cnt+1))



for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    visited = [0]*1000001
    waited = [(N,0)]
    visited[N] = 1
    print(f'#{tc}', end=' ')
    bfs()
    print()
