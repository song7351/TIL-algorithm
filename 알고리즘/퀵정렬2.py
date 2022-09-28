"""
기본원리
1. 리스트의 가장 처음을 pivot 기준으로 설정한다.
2. 남은 리스트의 왼쪽부터 기준보다 큰값을 찾고
2-1. 오른쪽부터 기준보다 작은값을 찾는다.
3. 두개전부 발견시 해당 값을 바꿔준다.
4. 진행시 교차되는 지점이 발견이되고
4-1. 교차될 경우 작은값을 pivot과 바꿔준다.

결과
왼쪽 pivot 오른쪽
왼쪽은 전부 pivot보다 작은수
오른쪽은 전부 pivot보다 큰수
그러면 다시 왼쪽에서 퀵정렬을 실행한다면?
그러면 다시 오른쪽에서 퀵정렬을 실행한다면?
-> 정렬 완료
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = []
    right_side = []
    for x in tail:
        if x <= pivot:
            left_side.append(x)
        else:
            right_side.append(x)

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


arr = [5,7,9,0,3,1,6,2,4,8]

arr2 = quick_sort(arr)
print(arr2)