"""
화물이 실려 있는 N개의 컨테이너를 M대의 트럭
트럭당 한 개의 컨테이너를 운반 할 수 있고,
트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행
테스트케이스
 첫 줄에 컨테이너 수 N과 트럭 수 M
  다음 줄에 N개의 화물이 무게wi,
  그 다음 줄에 M개 트럭의 적재용량 ti

화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다.
컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
최대 이동 화물무게는?
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    #컨테이너/화물트럭
    N,M = map(int, input().split())
    lst_N = list(map(int, input().split()))
    lst_M = list(map(int, input().split()))
    used_N = [0] * N

    ans = 0
    for i in range(M):          # 트럭 적재용량 성택
        select_N = -1
        idx = -1
        for j in range(N):      # 컨테이너 무게중 가장 큰것을 사용.
            if lst_M[i] >= lst_N[j] >= select_N:
                if used_N[j] == 0:  # 사용 기록이 없는것을 선택
                    idx = j
                    select_N = lst_N[j]

        if idx != -1:           # 만약 컨테이너를 선택했다면..
            used_N[idx] = 1     # 사용기록 남기고
            ans += select_N     # 더하세요.

    print(f'#{tc} {ans}')
