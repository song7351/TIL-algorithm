'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 
10 1 9 2 8 3 7 4 6 5
 
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    #정렬
    for i in range(N):
        for j in range(i+1, N):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    
    left = 0
    right = N-1
    print(f'#{tc}', end=' ')
    for i in range(5):
        print(num_list[right], end=' ')
        print(num_list[left], end=' ')
        right -= 1
        left += 1
    print()