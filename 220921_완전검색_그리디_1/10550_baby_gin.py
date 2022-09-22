"""
6자리 숫자에 대해서 완전 검색을 적용하여 baby-gin을 검사하세요.
baby-gin이란?
0~9가 적힌 카드중 6장을 받는다.
승리조건
1. 런: 3장의 카드가 연속적인 번호. 단 901은 제외
2. 트리플: 같은 번호를 가지는 3장의 카드

입력
124783
667767
053060
101123
"""
def f(i,N):
    global ans
    x = 0
    if i == N:
        front = lst[:3]
        back = lst[3:]
        if front[1] == front[0] + 1 == front[2] -1: # 3개가 연속된 수인가?
            x += 1
        if front[0] == front[1] == front[2]:        # 3개가 같은 수인가?
            x += 1
        if back[1] == back[0] + 1 == back[2] -1:
            x += 1
        if back[0] == back[1] == back[2]:
            x += 1
        if x == 2:
            ans = 'Baby Gin'
            return

    else:
        for j in range(i, N):       #p[i]에 들어갈 숫자 p[j]결정
            lst[i], lst[j] = lst[j], lst[i]
            f(i+1, N)
            lst[i], lst[j] = lst[j], lst[i]
test_case = int(input())

for tc in range(1, test_case + 1):
    lst = list(map(int, input()))
    ans = 'Lose'
    f(0, 6)
    print(f'#{tc} {ans}')