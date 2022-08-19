"""
N개의 상자(1번부터 ~ N번):  각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0

다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경

  ·  i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분되어 주어진다.

다음 Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)이 주어진다.
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N, Q = map(int, input().split())

    box = [0] * N

    for i in range(1,Q+1):
        L, R = map(int, input().split())

        for j in range(L-1, R):
            box[j] = i

    box = map(str, box)

    print(f'#{tc} {" ".join(box)}')