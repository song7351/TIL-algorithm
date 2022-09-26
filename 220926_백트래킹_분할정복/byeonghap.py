test_case = int(input())

def merge_sort(arr):
    global ans
    if len(arr) == 1:
        return arr

    m = len(arr)//2
    # 길이가 1일때 까지 왼쪽, 오른쪽으로 나눈다.
    left_arr = merge_sort(arr[:m])      # 그래서 최초에 4행값이 들어옴.
    right_arr = merge_sort(arr[m:])     # 그래서 최초에 4행값이 들어옴'

    if left_arr[-1] > right_arr[-1]:
        ans += 1

    merge_arr = []                      # 정렬한 결과
    i = j = 0
    while i < len(left_arr) and j < len(right_arr): # 어느한쪽이 다 나갈때까지.
        if left_arr[i] < right_arr[j]:
            merge_arr.append(left_arr[i])
            i += 1
        else:
            merge_arr.append(right_arr[j])
            j += 1

    merge_arr += left_arr[i:]       # 어느한쪽이 다 나간 상태이므로 나머지를 걍 리스트에 더한다.
    merge_arr += right_arr[j:]
    return merge_arr                # 해당 값을 리턴해줘서 9-10행으로 올라간다.

for tc in range(1, test_case + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    ans_lst = merge_sort(lst)
    print(f'#{tc} {ans_lst[N//2]} {ans}')