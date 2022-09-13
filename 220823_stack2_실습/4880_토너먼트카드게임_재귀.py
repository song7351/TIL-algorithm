"""
N명 : 가위바위보 토너먼트
가위1 바위2 보3
12 2 23 3 31 1
같다면, 번호(1~N)가 작은쪽이 승리
중간값을 기준으로 그룹을 2개로 쪼개서 시작.

"""
def RPS(arr, idx):
    # 중간값 = <(N+1)//2
    M = len(arr)
    if M == 2:
        if arr[0] == arr[1]:
            return arr[0], idx[0]
        elif arr[0] == 1 and arr[1] == 3:       # 가위, 보 일경우.
            return arr[0], idx[0]
        elif arr[0] < arr[1]:
            return arr[1], idx[1]
        elif arr[0] == 3 and arr[1] == 1:       # 보, 가위 일경우
            return arr[1], idx[1]
        else:
            return arr[0], idx[0]

    elif M == 1:
        return arr[0], idx[0]
    else:
        avg_M = (M+1)//2
        rps1, id1 = RPS(arr[:avg_M], idx[:avg_M])
        rps2, id2 = RPS(arr[avg_M:], idx[avg_M:])
        if rps1 == rps2:
            return rps1, id1
        elif rps1 == 1 and rps2 == 3:
            return rps1, id1
        elif rps1 < rps2:
            return rps2, id2
        elif rps1 == 3 and rps2 == 1:
            return rps2, id2
        else:
            return rps1, id1

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    game = list(map(int, input().split()))
    num = list( i for i in range(1, N+1))
    rps, idx = RPS(game, num)
    print(f'#{tc} {idx}')