'''
NxN배열에서 각 요소에 대해서, 그 요소와 이웃한 요소와의 차의 절대값에 대한 합을 구한 후,
총 합을 구하는 프로그램을 만드시오.
'''

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input()) # 배열크기
    arr_list = []    # 2차원 배열
    for i in range(N):
        arr = list(map(int, input().split()))
        arr_list.append(arr)
    
    di = [-1, 1, 0, 0]      #행, y축
    dj = [0, 0, -1, 1]      #열, x축
    total_sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):  #di, dj의 길이값 = 4
                ni = i + di[k]
                nj = j + dj[k]
                if 0<= ni < N and 0<= nj < N:   #최대범위 ( 0 ~ N )를 벗어나면 안됨.
                    #diff: 차이값, arr_list[i][j]: 기준값, arr_list[ni][nj]: 주변값
                    diff = arr_list[i][j] - arr_list[ni][nj]       #abs(value): 절대값
                    if diff <= 0:
                        diff = -diff
                    total_sum += diff
    
    print(f"#{tc} {total_sum}")