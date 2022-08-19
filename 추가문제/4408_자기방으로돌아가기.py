"""
// T : 테스트케이스 수
// N : 돌아가야 할 학생들의 수
// C : 현재 방, G : 돌아갈 방

"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    corridor = [0] * 200                        # 연속된 홀수짝수 두 수의 방은 같은 복도를 공유한다.
    for i in range(N):
        n1, n2 = map(int, input().split())
        if n1 % 2 == 0:                         # 복도 인덱스를 맞추기 위해서 짝수 일때 -1 을 실행.
            n1 = n1//2 - 1
        else:
            n1 = n1//2

        if n2 % 2 == 0:
            n2 = n2//2 - 1
        else:
            n2 = n2//2

        if n1 >= n2:                            # 복도 시작 인덱스와 도착 인덱스를 정하기위해서 크기 비교
            start = n2
            end = n1
        else:
            start = n1
            end = n2

        for j in range(start, end+1):           # 복도를 지나가면 +1
            corridor[j] += 1

    time = 0

    for i in range(200):
        if time < corridor[i]:                  # 복도에서 많이 겹칠수록 시간이 증가됨.
            time = corridor[i]

    print(f'#{tc} {time}')