test_case = int(input())

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

def quick_sort2(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left >= right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort2(arr, start, right-1)
    quick_sort2(arr, right+1, end)

for tc in range(1, test_case + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = quick_sort(arr)
    #print(ans)
    #quick_sort2(arr,0,N-1)
    #print(arr)
    print(f'#{tc} {ans[N//2]}')