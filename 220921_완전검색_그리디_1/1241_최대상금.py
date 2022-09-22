"""
숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.
1줄: 테스트케이스
N줄: n m : n숫자판 정보, m교환횟수

완전검색
각 깊이별 모든 경우를 탐색한다.
최대교환횟수 = 깊이
최대 자릿수 = 최대 겅우 = 6! = 720
"""
def f(i,N):
    global ans
    if i <= N:
        if i != 0:
            num = int(''.join(lst))
            if num > ans:
                ans = num
        for j in range(i,len(lst)):
            for k in range(j+1,len(lst)):
                lst[j], lst[k] = lst[k], lst[j]
                f(i+1, N)
                lst[j], lst[k] = lst[k], lst[j]

test_case = int(input())
for tc in range(1, test_case + 1):
    n,m = map(int, input().split())
    lst = list(str(n))
    visited = []
    ans = 0
    f(0,m)
    print(f'#{tc} {ans}')