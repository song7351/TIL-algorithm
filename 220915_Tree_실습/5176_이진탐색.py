"""
이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족
-> 중위순회 순서로 값을 집어넣는다.
루트 값과 N/2번 노드값을 표기해라
"""
def inorder(n):
    global num
    if n <= N:
        inorder(2*n)
        lst[n] = num
        num += 1
        inorder(2*n + 1)

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    lst = [0] * (N+1)
    num = 1
    inorder(1)
    print(f'#{tc} {lst[1]} {lst[N//2]}')