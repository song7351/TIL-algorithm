"""
N개의 수열
M번의 작업

첫줄 테스트케이스
2번: N, M
3번: 수열
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    suyeol = list(map(int, input().split()))
    cnt = 1
    while cnt <= M:
        suyeol.append(suyeol.pop(0))
        cnt += 1

    print(f'#{tc} {suyeol[0]}')