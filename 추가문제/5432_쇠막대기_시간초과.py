"""
여러 개의 쇠막대기를 레이저로 절단하려고 한다.

효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.

쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.

 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.

 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.

 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

아래 그림은 위 조건을 만족하는 예를 보여준다.

수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.

이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.

    1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다. 또한, 모든 “()”는 반드시 레이저를 표현한다.

    2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.

위 예의 괄호 표현은 그림 위에 주어져 있다.

쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고,

이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.

쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하라.
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    board = list(input())
    N = len(board)
    # 쇠막대기 각각 열고닫는 리스트
    board_list = [1] * N
    for i in range(1,N-1):
        if board[i-1] != board[i]:
            board_list[i] = board_list[i-1]
        else:
            if board[i] == '(':
                board_list[i] = board_list[i-1] + 1
            else:
                board_list[i] = board_list[i-1] - 1

    total_cnt = 0
    for i in range(N-1):
        start_idx = i
        target = board_list[i]
        if board[start_idx] != "(":
            continue
        while board_list[i+1] != target:
            i += 1
            if i >= N-1:
                break
        end_idx = i+1
        if end_idx - start_idx == 1:
            continue
        cnt = 1
        for j in range(start_idx, end_idx-1):
            if board_list[j] == board_list[j+1]:
                if board[j] == "(" and board[j+1] == ")":
                    cnt += 1
        total_cnt += cnt

    print(f'#{tc} {total_cnt}')