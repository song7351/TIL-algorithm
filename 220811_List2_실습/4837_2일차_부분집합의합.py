'''
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.

책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

'''
test_case = int(input())

for tc in range(1, test_case+1):
    total_page, target_a, target_b = map(int, input().split())
    
    # A계산
    start = 1
    end = total_page
    cnt_a = 0
    while start <= end:
        middle = int((start+end)/2)
        cnt_a += 1
        if middle == target_a:
            break
        elif middle > target_a:
            end = middle
        else:
            start = middle
        
    # B계산
    start = 1
    end = total_page
    cnt_b = 0
    while start <= end:
        middle = int((start+end)/2)
        cnt_b += 1
        if middle == target_b:
            break
        elif middle > target_b:
            end = middle
        else:
            start = middle

    ans = 0
    if cnt_a < cnt_b:
        ans = 'A'
    elif cnt_a > cnt_b:
        ans = 'B'

    print(f'#{tc} {ans}')