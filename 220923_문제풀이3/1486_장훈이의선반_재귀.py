"""
탑의 높이가 B 이다.
B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.
1줄: 테스트케이스
2줄: N명 목표B
3줄: Ni ~
"""

test_case = int(input())

def f(i,k,s):
    global ans,B
    if i == k:
        #for j in range(k):
            #if bit[j]:
                #print(lst[j], end=" ")
        if B <= s < ans:
            ans = s
        #print(s)
        #print()
        pass
    elif s > ans:
        return
    else:
        bit[i] = 0
        f(i+1, k, s+lst[i])
        bit[i] = 1
        f(i+1, k, s)

for tc in range(1, test_case + 1):
    N, B = map(int,input().split())
    lst = list(map(int,input().split()))
    bit = [0] * N
    ans = 200000
    ## 1. 부분집합의 합 ##
    f(0,N,0)

    print(f'#{tc} {ans-B}')