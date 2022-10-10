"""

"""
def f(i,s):
    global ans
    if i > 12:
        if ans > s:
            ans = s
    else:
        f(i+1, s+min(d*year[i],m1))
        f(i+3, s+m3)

test_case = int(input())

for tc in range(1, test_case + 1):
    d, m1, m3, y = map(int, input().split())
    year = [0] + list(map(int, input().split()))
    ans = y
    f(1,0)
    print(f'#{tc} {ans}')