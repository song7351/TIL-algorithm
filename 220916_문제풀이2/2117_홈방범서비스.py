"""
N*N 크기의 도시
서비스 영역의 크기 K = 대각선길이가 N인 마름모
** 입력 **
//총 테스트 케이스 개수 T=10
//첫 번째 테스트 케이스, N=8, M=3
//도시 맵, 1은 집
M = 한집당 지불가능한 비용

수익이 발생할때, 집이 가장 많은것을 출력하라.
크기가 K일때 비용은 k^2 + (k-1)^2
방법1. 훑으면서 집에 걸릴때마다 확장 확인
방법2. 집리스트를 따로 만들어서 한다.
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N,M = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    house = []
    ans = 0
    for i in range(N):                  # 집좌표들 보관하기
        for j in range(N):
            if board[i][j] == 1:
                house.append([i,j])
    for i in range(N):
        for j in range(N):              # 서비스 시작할 위치
            distance = []               # 서비스 중심지로부터 집들과의 거리
            for a,b in house:
                distance.append(abs(a-i)+abs(b-j))
            k = max(distance)           # 서비스 중심지로부터 가장 먼거리
            cnt = len(distance)         # 총 집의 개수
            for l in range(k,-1, -1):    # 가장 먼거리부터 서비스실시
                cost = (l+1)**2 + l**2  # 서비스 실제비용은 거리+1해서 계산
                cnt -= distance.count(l+1)  # 해당 거리보다 큰건 지속적으로 집에서 제거
                profit = cnt*M - cost       # 그래서 수익이 마이너스가 아닌가?
                if profit >= 0:
                    if cnt > ans:           # 더 많은 집이 혜택을 받는가?
                        ans = cnt

    print(f'#{tc} {ans}')