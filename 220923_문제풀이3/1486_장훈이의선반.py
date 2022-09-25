"""
탑의 높이가 B 이다.
B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.
1줄: 테스트케이스
2줄: N명 목표B
3줄: Ni ~
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N, B = map(int,input().split())
    lst = list(map(int,input().split()))
    idx = [i for i in range(N)]

    ## 1. 부분집합으로 접근? ##
    ziphap = [[]]
    for i in idx:
        for j in range(len(ziphap)):
            ziphap.append(ziphap[j] + [i])

    ans = 200000
    for i in range(1,len(ziphap)):
        s = 0
        for j in ziphap[i]:
            s += lst[idx[j]]
        if B <= s < ans:
            ans = s

    print(f'#{tc} {ans-B}')