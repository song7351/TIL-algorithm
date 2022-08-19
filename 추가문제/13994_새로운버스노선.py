"""
종류: 일반, 급행, 광역
모든 정류장은 1번부터 1000번

모든 버스는 A번에서 출발해 B번까지 운행
일반버스는 A번부터 B번 사이의 모든 정류장에 정차
급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 짝수 번호 정류장에 정차
          A가 홀수인 경우 A와 B사이의 모든 홀수 번호 정류장에 정차
광역 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장,
              A가 홀수인 경우 A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장

최대 몇 개의 노선이 같은 정류장에 정차

1               테스트케이스
3               N = 노선의 수 1~100
1 2 5           버스 타입 (1 일반, 2 급행, 3 광역 급행), 출발A, 도착B
2 3 10
3 2 9
"""
test_case = int(input())

for tc in range(1, test_case + 1):

    stop = [0] * 1000

    N = int(input())
    for _ in range(N):
        bus, start, end = map(int, input().split())
        if bus == 1:
            for i in range(start, end + 1):
                stop[i - 1] += 1
        elif bus == 2:
            if start % 2 == 0:
                for i in range(start, end + 1):
                    if i % 2 == 0:
                        stop[i - 1] += 1
            else:
                for i in range(start, end + 1):
                    if i % 2 != 0:
                        stop[i - 1] += 1
        else:
            if start % 2 == 0:
                for i in range(start, end + 1):
                    if i % 4 == 0:
                        stop[i - 1] += 1
            else:
                for i in range(start, end + 1):
                    if i % 3 == 0 and i % 10 != 0:
                        stop[i - 1] += 1

    ans = stop[0]
    for i in stop:
        if ans < i:
            ans = i

    print(f'#{tc} {ans}')
