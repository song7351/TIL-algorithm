"""
 5,000개의 버스 정류장 ( 1 ~ 5000 )
 버스 노선은 N개
 i번째 버스 노선은 번호가 Ai이상이고 Bi이하인 모든 정류장만을 다니는 버스 노선

 P개의 버스 정류장, 각 정류장에 몇 개의 버스 노선이 다니는지 ?

 N ( 1 ≤ N ≤ 500 )
 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )
 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 )

"""

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())    # 버스노선 개수
    A = []              # i번 버스는 Ai <= 버스노선 <= Bi
    B = []
    C = [0] * 5000             # i = i-1번 버스정류장.
    for _ in range(N):
        a,b = map(int, input().split())
        for j in range(a-1, b):
            C[j] += 1
    P = int(input())        # 삼성시 정류장 개수

    print(f"#{tc}", end=" ")

    for j in range(P):
         c = int(input())
         print(C[c-1], end=" ")
    print()