"""
절반씩 직접 슬라이싱 하는것보다, 원본크기의 리스트를 만들어서 관리하는게 더 소모가 적음

"""
def msort(i,N):                 # 병합구간의 시작인덱스, 구간의 원소개수
    if i == N:                  # 분할할 원소의 개수가 1개일경우.
        return
    else:
        msort(i, N//2)          # 왼쪽리스트의 시작인덱스, 구간의 원소개수
        msort(i+N//2, N//2)     # 오른쪽리스트의 시작인덱스, 구간의 원소개수
        k = 0
        l,r = i, i + N//2
        while l<i+N//2 and r<i+N: # 왼쪽구간에서 비교위치 and 오른쪽 구간에서 비교위치
            if arr[l] <= arr[r]:     # 왼쪽이 더 작은가?
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1

        # while문이 끝났다? == 왼쪽 혹은 오른쪽 구간에 남은 숫자가 없다.
        while l< i + N//2:
            tmp[k] = arr[l]
            l += 1
            k += 1
        while r < (i+N):
            tmp[k] = arr[r]
            r += 1
            k += 1

        for k in range(N):
            arr[i+k] = tmp[k]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]*N
    msort(0,N)
    print(arr)