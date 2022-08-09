'''
(문제 생략)
단, 방의 가로 길이는 N이다.  

입력으로 테스트케이스 개수, 다음 줄부터 케이스별로 첫 줄에 N, 다음 줄에 N개의 상자 높이가 주어진다.
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if maxV < cnt:
            maxV = cnt
    print(f'#{tc} {maxV}')