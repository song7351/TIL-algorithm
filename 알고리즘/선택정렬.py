"""
가장 앞자리부터 작은순서대로 정렬을 한다.
복잡도 O(n^2)
"""

lst = [0,1,2,3,4,5]

def SelectionSort(arr):
    n = len(arr)
                                                    # 가장 앞자리부터 우선 작은수를 채운다
    for i in range(0, n-1):                         # 우선 앞자리 선택         
        minI = i                
        for j in range(i+1, n):                     # 이후 뒷자리들 중에서 가장 작은 값을 찾는다
            if arr[j] < arr[minI]:
                minI = j
        arr[i], arr[minI] = arr[minI], arr[i]       # 반복문 끝 = 가장 작은값 발견 => 교환실행

"""
[3,4,2,1,5]
3 [4,2,1,5]
4>3
2<3
1<2
5>1
3 1
-----------
[1,4,2,3,5]
4 [2,3,5]
반복...
"""