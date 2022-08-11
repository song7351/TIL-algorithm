'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
'''

test_case = int(input())

for tc in range(1, test_case+1):
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    N, target = map(int, input().split())
    cnt = 0
    ans_list = []
    #부분집합 
    for i in range(1<<12):
        target_list = []
        sum_nums = 0
        for j in range(12):
            if i & (1<<j):
                sum_nums += A[j]
                target_list.append(A[j])
        #조건 합 == target, 길이 = N
        if sum_nums == target and len(target_list) == N and target_list not in ans_list:
            ans_list.append(target_list)
            cnt += 1
    
    print(f'#{tc} {cnt}')