"""
양의 정수 N에 대해 N = X^3가 되는 양의 정수X
첫 번째 줄에 테스트 케이스의 수 T
*출력*
N = X3가 되는 양의 정수 X를 출력한다.
만약 이런 X가 존재하지 않으면 -1을 출력한다.
*입력*
첫 번째 줄에는 하나의 정수 N(1≤N≤10^18) 이 주어진다.

3// 총 테스트 케이스 개수 T=1
27// 첫 번째 테스트케이스, N=27
7777// 두 번째 테스트케이스
64
"""
"""
방법 1.
0 ~ 10^6 짜리 배열에
각자리의 3승을 값으로 설정
N을 찾는 이진탐색.
방법 2.
1/3승 후 3승해서 N이 나오는가?
"""
test_case = int(input())

lst = [i**3 for i in range(10**6 + 1)]

for tc in range(1, test_case + 1):
    N = int(input())
    s,e = 0, 10**6
    while s <= e:
        idx = (s+e)//2
        if N == lst[idx]:
            break
        if N > lst[idx]:
            s = idx+1
        else:
            e = idx-1

    if N != lst[idx]:
        idx = -1

    print(f'#{tc} {idx}')