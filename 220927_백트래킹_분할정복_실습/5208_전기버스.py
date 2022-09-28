test_case = int(input())
def f(start,end,cnt):
    global ans
    if start >= end:
        if cnt < ans:
            ans = cnt
    elif cnt > ans:
        return
    else:
        x = lst[start]
        while x:
            f(start+x, end, cnt + 1)
            x -= 1

for tc in range(1, test_case + 1):
    lst = list(map(int, input().split()))
    ans = 200
    f(1,lst[0],-1)          # 처음과 도착은 횟수에서 제외
    print(f'#{tc} {ans}')