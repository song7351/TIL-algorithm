'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
v12345
v12345
이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
v12345
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.
----------------------------------------------------------------------------------------
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
'''

test_case = int(input())

for tc in range(1,test_case+1):
    N, M = map(int, input().split())    # N: 정수의 개수, M: 구간의 개수
    max_sum = N * 1                     # 최소값 1 * 입력 숫자 개수
    min_sum = N * 10000                 # 최대값 10000 * 입력 숫자 개수
    num_list = list(map(int, input().split()))
    
    for i in range(N-M+1):              # 입력값 확인 범위는 0부터 N개 - M구간개수 + 1(range범위에 따라 +1)
        num_sum = 0                     # 최초의 합
        for j in range(i, i+M):         # 검사할 범위 = 구간범위 M
            num_sum += num_list[j]
        if num_sum > max_sum:           # 구간합이 max_num보다 크다면 max_num값
            max_sum = num_sum
        if num_sum < min_sum:           # 구간합이 min_num보다 작다면 min_num값
            min_sum = num_sum
    
    print(f"#{tc} {max_sum-min_sum}")