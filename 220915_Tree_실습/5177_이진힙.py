"""
이진 최소힙은 다음과 같은 특징을 가진다.

    - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.

    - 부모 노드의 값<자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우,
    조건을 만족할 때까지 부모 노드와 값을 바꾼다.

    - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.

** 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성 **
첫줄: 테스트케이스
2줄: N -자연수 개수
3줄: N개의 자연수
5 <= N <= 500
Ni <= 10000
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0, lst[0]]
    for i in range(1, N):
        heap.append(lst[i])                         # 이진힙 = 일단 맨 마지막 노드 추가
        c = len(heap) - 1                           # 자식노드 idx
        p = c // 2                                  # 부모노드 idx = 자식노드 // 2
        while p and heap[p] > heap[c]:              # 부모idx가 0인건 없음, 부모노드는 자식노드보다 항상 작아야됨.
            heap[p], heap[c] = heap[c], heap[p]
            c = p                                   # 부모노드보다 작다면 바꾼뒤 아닐때까지 계속 확인
            p = c//2
    c2 = N
    ans = 0
    while c2:                                       # 부모노드의 합
        c2 = c2 // 2
        ans += heap[c2]
    #print(heap)
    print(f'#{tc} {ans}')

