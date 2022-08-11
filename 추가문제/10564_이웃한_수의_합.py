'''
N개의 정수에서 이웃한 두 수의 합이 최대인 경우와 최소인 경우를 찾아 출력하시오. 예를 들어 5개의 정수 3 2 1 4 5의 경우, 이웃한 수의 합은 5, 3, 5, 9이므로 이중 최대와 최소인 9, 3을 출력한다.

입력

첫 줄에 테스트케이스 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N, 다음 줄에 절대값10억 이하의 정수 N개가 빈 칸으로 구분되어 주어진다.

1<=T<=10, 5<=N<=1000
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    max_num = -2000000000
    min_num = 2000000000
    
    for i in range(N-1):
        sum_num = num_list[i] + num_list[i+1]
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < min_num:
            min_num = sum_num
        
    print(f'#{tc} {max_num} {min_num}')