"""
사탕수량 묶음수량
ex) 10 3
10개를 3묶음으로 나눴을때 각 수의 곱중 가장 큰값은?
1 1 8 => 8
3 3 4 => 36
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N, P = map(int, input().split())
    # 최대 곱이 나오기 위해서는 모든 묶음의 수량이 중간값에 가까워야 한다.
    avg_candy = N//P
    if N % P != 0:
        namerg = N % P
        ans = (avg_candy+1)**namerg * avg_candy**(P - namerg)
    else:
        ans = avg_candy ** P

    print(f'#{tc} {ans}')