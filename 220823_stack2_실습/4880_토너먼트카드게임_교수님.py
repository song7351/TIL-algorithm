def win(left, right):
    if game[left] == game[right]:               # 가위바위보를 비길경우 무조건 왼쪽(인덱스가 작은쪽)
        return left
    elif game[left] - game[right] in [1, -2]:   # 왼쪽이 이기는 경우 = 두 수의 차가 1 or -2일 경우
        return left
    else:
        return right

def f(i, j):                        # i~j번까지의 승자를 찾는 함수
    if i==j:                        # 한 명만 남은 경우
        return i
    else:                           # 두 명 이상인 경우 두 그룹의 승자를 찾아 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    game = list(map(int, input().split()))

    ans = f(0, N-1)
    print(f'#{tc} {ans+1}')