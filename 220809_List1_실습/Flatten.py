'''
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
'''

test_case = 10

for tc in range(1, test_case+1):
    dump_cnt = int(input())
    box_list = list(map(int, input().split()))  #길이 100의 박스리스트
    
    while dump_cnt >= 0:                    #dump_cnt가 0이되면 동작을 멈춰야한다.
        max_heigh = 1
        max_idx = 0
        min_heigh = 100
        min_idx = 0
        
        for i in range(100):                #박스의 길이는 100이다
            if box_list[i] >= max_heigh:    #최대 높이, 인덱스
                max_heigh = box_list[i]
                max_idx = i
                
            if box_list[i] <= min_heigh:    #최소 높이, 인덱스
                min_heigh = box_list[i]
                min_idx = i
                      
        if dump_cnt == 0:                   #dump_cnt가 0이되면 동작을 멈춰야한다.
            print(f'#{tc} {max_heigh - min_heigh}')
            break
        
        box_list[max_idx] = max_heigh - 1   #최대높이에 해당하는 인덱스 값을 -1
        box_list[min_idx] = min_heigh + 1   #최소높이에 해당하는 인덱스 값을 +1
        dump_cnt -= 1                       #최대, 최소 높이 조정했으면 dump값은 1감소