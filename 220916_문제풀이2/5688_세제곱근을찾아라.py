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
test_case = int(input())


for tc in range(1, test_case + 1):
    N = int(input())
    x = 1
    while x*x*x <= N:
        if x*x*x == N:
            break
        else:
            x += 1
    if x*x*x > N:
        x = -1

    print(f'#{tc} {x}')