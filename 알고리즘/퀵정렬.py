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

def quick_sort(arr, start, end):
    if start >= end:    # 시작지점이 끝점보다 같거나 클 경우, 종료
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left >= right:   # 엇갈렸다면,
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start,right-1)
    quick_sort(arr, right+1, end)

arr = [5,7,9,0,3,1,6,2,4,8]

quick_sort(arr, 0, len(arr)-1)
print(arr)