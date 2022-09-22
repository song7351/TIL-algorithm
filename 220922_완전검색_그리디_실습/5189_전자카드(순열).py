"""
1줄: 테스트케이스
2줄: N 사무실크기
N줄: 사무실정보
N <= 10, Ni <= 100
"""

def f(i, N):
    global ans
    if i == N:                              # 최대이동에 도달했을때
        n = 0
        test = lst + [lst[0]]
        for j in range(len(test)-1):
            n += board[test[j]][test[j+1]]
        #print(n)
        if n < ans:
            #print(test)
            ans = n
    else:
        for j in range(i,N):
            lst[i], lst[j] = lst[j], lst[i]
            if lst not in visited[i]:
                f(i+1, N)
                visited.append(lst)
            lst[i], lst[j] = lst[j], lst[i]

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[] for _ in range(N+1)]
    ans = 100*10
    lst = [ i for i in range(N)]    # 방 이동 경로
    f(0, N-1)                         # f(현재 이동횟수, 도착 이동횟수)
    print(f'#{tc} {ans}')