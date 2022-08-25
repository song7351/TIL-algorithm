"""
N 개의 피자를 동시에 진행
M 개의 피자(1~M번)를 작업

조건
- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.
- 3<=N<=20, N<=M<=100, 1<=Ci<=20

"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    cheese_idx = list(i for i in range(1,M+1))
    hwadeog = []
    hwadeog_idx = []

    for i in range(N):
        hwadeog.append(cheese.pop(0))
        hwadeog_idx.append(cheese_idx.pop(0))

    flag = 0
    ans = 0
    while flag == 0:
        for i in range(N):
            front = hwadeog.pop(0)
            front_idx = hwadeog_idx.pop(0)
            if front != 0:
                front = front//2
                if front == 0 and cheese:
                    hwadeog.append(cheese.pop(0))
                    hwadeog_idx.append(cheese_idx.pop(0))
                else:
                    hwadeog.append(front)
                    hwadeog_idx.append(front_idx)
                    if front == 0:
                        cnt = 0
                        for j in range(N):
                            if hwadeog[j] == 0:
                                cnt += 1
                            else:
                                ans = hwadeog_idx[j]
                        if cnt == N-1:
                            flag = 1
                            break
            else:
                hwadeog.append(front)
                hwadeog_idx.append(front_idx)

    print(f'#{tc} {ans}')