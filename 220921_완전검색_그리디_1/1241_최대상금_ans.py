"""
숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.
1줄: 테스트케이스
N줄: n m : n숫자판 정보, m교환횟수

완전검색
각 깊이별 모든 경우를 탐색한다.
최대교환횟수 = 깊이
최대 자릿수 = 최대 겅우 = 6! = 720

# 중요개념 : 메모이제이션
-> 여기서는 각 깊이(행)에따라 열에 기록을 남긴다.
"""
def swap(prize, i, j):
    # 리스트만들기(str)
    prize_arr = [0] * prize_len
    for k in range(prize_len-1, -1, -1):
        prize_arr[k] = prize % 10
        prize //= 10
    # swap
    prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]

    # int 만들기
    prize = 0
    for k in range(prize_len):
        prize = prize * 10 + prize_arr[k]

    return prize

def f(n,k,prize):       # k는 깊이
    global ans, cnt
    cnt += 1
    ####가지치기####
    for i in range(720):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:   # 만약 같은게 있으면? 다시 위로 올라가세요.
            return
    ##############
    if n == k:
        # 최대값 유지
        if prize > ans:
            ans = prize
    else:   # 숫자판길이에서 2개를 선택
        for i in range(prize_len-1):
            for j in range(i+1, prize_len):
                f(n, k+1, swap(prize, i ,j)) 
    pass

test_case = int(input())
for tc in range(1, test_case + 1):
    prize, N = map(int, input().split())
    memo = [[0]* 720 for _ in range(N+1)]   # 깊이최대N, 최대길이는 6! = 720
    # 숫자판의 길이
    prize_len = 0
    t = prize
    while t:
        t //= 10
        prize_len += 1

    ans = 0
    #cnt = 0
    f(N,0,prize)
    #print(cnt)
    print(f"#{tc} {ans}")