"""
    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.
    ex)  3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익

    자연수 N(2 ≤ N ≤ 1,000,000)
    매매가를 나타내는 N개의 자연수
    각 날의 매매가는 10,000이하
"""
def sajaegi(arr):
    if len(arr) == 1:                       # 리스트의 길이가 1이라면 안산다.
        return 0

    max_cost = arr[0]
    max_idx = 0

    for i in range(len(arr)):               # 최고값과 그 인덱스를 구한다.
        if arr[i] >= max_cost:
            max_cost = arr[i]
            max_idx = i

    arr1 = arr[:max_idx+1]                  # 최고값을 포함한 이전의 리스트에서 수익을 구한다.
    benefit = 0
    for i in range(len(arr1)-1):
        benefit += (arr1[-1] - arr1[i])
    if max_idx == len(arr)-1:               # 만약 최고값이 리스트의 마지막에 있다면 단순히 수익을 리턴
        return benefit
    else:
        arr2 = arr[max_idx+1:]              # 뒤에 리스트가 더 있다면 재귀함수 실행.
        return benefit + sajaegi(arr2)

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    market = list(map(int, input().split()))

    ans = sajaegi(market)

    print(f'#{tc} {ans}')

