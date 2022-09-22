"""
목적: 최대 몇 대의 화물차가 이용
, 앞 작업의 종료와 동시에 다음 작업을 시작가능
1줄: 테스트케이스
2줄: 신청서 N
N줄: 작업 시작 시간 s와 종료 시간 e
0<= s < 24
0<= e <= 24
"""
test_case = int(input())

def f(n):
    global ans
    ans += 1
    for i in range(n+1, len(lst)):
        if lst[i][0] >= lst[n][1]:
            f(i)
            return

for tc in range(1, test_case + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    time_lst = [0] * 24
    lst.sort(key=lambda x: (x[1])) # 가장 종료시간이 빠른순서 정렬

    ans = 0
    f(0)

    #print(lst)
    print(f'#{tc} {ans}')