"""
1에서 5,000까지 번호
 버스 노선은 N개
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    C = [0]*5001
    for _ in range(N):
        x,y = map(int, input().split())
        for i in range(x,y+1):
            C[i] += 1

    P = int(input())
    print(f'#{tc}', end=' ')
    for i in range(P):
        x = int(input())
        print(C[x], end=' ')
    print()
