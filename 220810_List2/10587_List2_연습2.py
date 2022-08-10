'''
10개의 정수를 입력 받아 부분 집합의 합이 0이 되는지 확인하는 프로그램을 만드시오.

입력

첫 줄에 테스트케이스 T, 다음 줄부터 테스트케이스 별로 절대값 1이상 20이하의 정수 10개가 제공된다.

1<=T<=10

출력

#과 테스트케이스 번호, 빈칸에 이어 부분집합의 합이 0이되는 경우가 있으며 1, 아니면 0을 출력한다.
'''
test_case = int(input())

for tc in range(1, test_case+1):
    arr = list(map(int, input().split()))   #테스트할 리스트값
    N = len(arr)  #문제에서 제공된 조건. 정수는 10개 제공

    #부분집합 만들기
    ans = 0
    flag = 0
    for i in range(1<<N):
        ans = 0
        for j in range(N):
            if i & (1<<j):
                ans += arr[j]
                if ans == 0:
                    flag = 1
                    print(f'#{tc} 1')
                    break
        if flag == 1:
            break
    else:
        print(f'#{tc} 0')
    
        

