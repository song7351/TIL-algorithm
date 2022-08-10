'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
'''

test_case = int(input())

for tc in range(1,test_case+1):
    N = int(input()) #달팽이 크기
    house = [list([0]*N) for _ in range(N)] #달팽이 집
    cnt_list = []
    for i in range(N, 0, -1):
        if i == N:
            cnt_list.append(i)
        else:
            cnt_list.append(i)
            cnt_list.append(i)
    y = 0
    x = -1
    num = 0
    for i in range(len(cnt_list)):
        if i % 4 == 0: #오른쪽
            for j in range(cnt_list[i]):
                x += 1
                num += 1
                house[y][x] = num
        elif i % 4 == 1: #아래
            for j in range(cnt_list[i]):
                y += 1
                num += 1
                house[y][x] = num
        elif i % 4 == 2: #왼쪽
            for j in range(cnt_list[i]):
                x -= 1
                num += 1
                house[y][x] = num
        elif i % 4 == 3: #위
            for j in range(cnt_list[i]):
                y -= 1
                num += 1
                house[y][x] = num
    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(house[i][j], end=" ")
        print()