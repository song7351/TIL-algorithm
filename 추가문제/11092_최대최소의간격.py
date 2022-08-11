'''
N개의 양의 정수가 첫번째부터 N번째까지 주어진다. 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 하시오. 단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.
예를 들어, {1, 1, 2, 3, 3} 가 주어지면 최대값의 위치는 5이고, 최소값의 위치는 1이다. 따라서 두 값 차이의 절대값은 4이다.
'''
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    max_num = 0
    max_idx = -1
    min_num = 10000000000000000000
    min_idx = -1
    for i in range(N):
        if num_list[i] >= max_num:
            max_num = num_list[i]
            max_idx = i
        if num_list[i] < min_num:
            min_num = num_list[i]
            min_idx = i
    diff = max_idx - min_idx
    if diff < 0:
        diff = -diff
    print(f'#{tc} {diff}')