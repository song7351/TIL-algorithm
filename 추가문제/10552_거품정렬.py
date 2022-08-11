'''
N개의 정수를 거품 정렬을 사용해 오름차순으로 정렬할 때, 두 수의 자리를 바꾼 횟수를 출력하시오. 두 정수의 크기가 같을 때는 자리를 바꾸지 않는다.
입력 첫 줄에 테스트케이스 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N, 다음 줄에 0이상 10억이하의 정수 N개가 빈 칸으로 구분되어 주어진다.
1<=T<=10, 5<=N<=1000
'''
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    #버블 정렬 오름차순.
    for i in range(N):
        for j in range(0, N-1-i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                cnt += 1
                
    print(f'#{tc} {cnt}')
