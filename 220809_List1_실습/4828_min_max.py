'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

test_case = int(input())

for tc in range(1,test_case+1):
    N = int(input())
    max_num = 1         #문제 조건 범위의 최소값
    min_num = 1000000   #문제 조건 범위의 최대값
    num_list = list(map(int, input().split()))  # 입력값을 list로 받는다.
    for i in range(N):
        if num_list[i] > max_num:   # 최대값 보다 크다면 최대값
            max_num = num_list[i]
        
        if num_list[i] < min_num:   # 최소값 보다 작다면 최소값
            min_num = num_list[i]
    print(f"#{tc} {max_num-min_num}")