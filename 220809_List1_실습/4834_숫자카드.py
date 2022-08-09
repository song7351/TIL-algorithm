'''
문제 원본은 입력 파일이 윈도우즈 텍스트 형식으로 되어 있어 다음 방식으로 읽을 수 없습니다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input())) # 윈도우즈 텍스트 형식은 이 부분에서 에러 발생함.
    ...
제출용 문제는 입력 파일을 리눅스 텍스트 형식으로 저장했기 때문에 위의 코드로 정상적으로 읽을 수 있습니다.
'''

test_case = int(input())

for tc in range(1,test_case+1):
    N = int(input())
    cnt_list = [0]*10
    max_cnt = 0
    
    num_list = list(map(int, input()))  # 입력값을 list로 받는다.
    for i in range(N):
        cnt_list[num_list[i]] += 1      # 각 값 = idx, 갯수 = value cnt_list를 만든다.

    for j in range(10):
        if cnt_list[j] >= max_cnt:      # cnt_list에서 가장 큰값 = 가장 많이 나온 횟수
            max_cnt = cnt_list[j]       # 가장 많이 나온 횟수의 카드값 = idx
            num = j

    print(f"#{tc} {num} {max_cnt}")