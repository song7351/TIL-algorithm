"""
N^2개의 방이 N×N형태로 늘어서 있다.
i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j
상하좌우에 있는 다른 방으로 이동
이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지
1줄: 테스트케이스
2줄: 하나의 정수 N (1 ≤ N ≤ 10^3)
N줄: 크기 N인 방모양과 각 방의 크기값존재

**출력**
가장 많이 이동가능한 출발점의 값을 구하여라
만약, 가장 많이 이동가능한 값이 같다면, 출발점중 더 작은 수를 출력해라.
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    ni = [-1,1,0,0]
    nj = [0,0,-1,1]
    max_cnt = 1
    room = 10**3
    for i in range(N):          # 방검사
        for j in range(N):
            cnt = 1  # 이동횟수
            room_num = board[i][j]
            x,y = i,j
            limit = 4
            while limit > 0:
                for k in range(4):  # 4방향 검사
                    di = x + ni[k]
                    dj = y + nj[k]
                    if 0<= di < N and 0<= dj < N:
                        if board[di][dj] == board[x][y] + 1:   # 방번호보다 1크다면 이동해라
                            x,y = di,dj
                            cnt += 1
                            limit = 4
                            break
                        else:
                            limit -= 1
                    else:
                        limit -= 1

            if cnt > max_cnt:
                max_cnt = cnt
                room = room_num

            elif cnt == max_cnt:
                if room > room_num:
                    room = room_num

    print(f'#{tc} {room} {max_cnt}')