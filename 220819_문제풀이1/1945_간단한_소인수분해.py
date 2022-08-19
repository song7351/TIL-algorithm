"""
N=2^a x 3^b x 5^c x 7^d x 11^e

print #tc a b c d e
"""

test_case = int(input())

for tc in range(1, test_case+1):
    num = int(input())
    ans = [0] * 5           # [a,b,c,d,e] 리스트

    while num != 1:
        if num % 11 == 0:
            num //= 11
            ans[4] += 1
        if num % 7 == 0:
            num //= 7
            ans[3] += 1
        if num % 5 == 0:
            num //= 5
            ans[2] += 1
        if num % 3 == 0:
            num //= 3
            ans[1] += 1
        if num % 2 == 0:
            num //= 2
            ans[0] += 1
    ans = map(str, ans)
    print(f"#{tc} {' '.join(ans)}")