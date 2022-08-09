'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
'''

test_case = int(input())

for tc in range(1,test_case+1):
    K, N, M = map(int, input().split())             # K: 최대이동거리 ,N: 정류장 개수 ,M: 충전기 개수
    bus_stop = [0] * (N+1)                              # bus_stop: 정류장 리스트
    charger_list = list(map(int, input().split()))  # charger_list: 충전기가 설치된 idx, 개수는 M개
    
    for i in charger_list:
        bus_stop[i] = 1
        
    cnt = 0
    start = 0
    end = K
    for i in range(M):                              # 최대 횟수는 정류장 수량만큼.
        for j in range(end, start-1, -1):           # 최소값을 구해야 하므로 끝거리에서 시작거리로 역순을 구한다.
            if end >= N:                            # 여기서 j는 현재 위치를 뜻한다
                break                               # end가 도착지(N)보다 크다면 자동으로 도착지(N)에 갈수 있다는것을 의미
            
            if bus_stop[j] == 1:                    # 현재위치가 충전소위치라면
                start = j                           # 시작점은 충전소위치
                end = j+K                           # 최대도착지점은 충전소위치 + 최대이동거리
                cnt += 1                            # 횟수 +1
                break

    if end >= N:                                    # 반복문 결과: end가 도착지(N)보다 크다면 자동으로 도착지(N)에 갈수 있다는것을 의미
        print(f"#{tc} {cnt}")
    else:
        print(f"#{tc} 0")                           # 반복문 결과: end가 도착지(N)보다 작다면 도착하지 못했음을 의미
        
                
            