"""
두 기차 A, B가 서로를 향해 달리고 있다.
거리는 250
기차 A는 시속 10마일, B는 시속 15마일
파리가 기차 A의 전면부에서 기차 B로 시속 20마일의 속력
파리가 기차 B의 전면부에 닿으면 바로 방향을 바꿔
기차 A를 향해 같은 속력으로 날아간다.

두기차 거리가 0이면 파리는 죽는다.
이때 파리의 최종 일반 거리는?
D는 두 기차 전면부 사이의 거리, A는 기차 A의 속력, B는 기차 B의 속력, F는 파리의 속력이다.
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)  # 파리는 기차가 부딪칠때까지 날 수 있다.
    distance = F * time
    print(f'#{tc} {distance}')
