"""
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.
-> 후위 순회
노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
"""
# import sys; sys.stdin = open('5178_노드합.txt')

def postorder(n):
    if n<= N:
        postorder(2*n)
        postorder(2*n + 1)
        if lst[n] == 0:
            if 2*n <= N:                    # 자식노드가 없으면 error발생
                lst[n] += lst[2*n]
            if 2*n + 1 <= N:
                lst[n] += lst[2*n + 1]

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M, L = map(int, input().split())
    lst = [0] * (N+1)
    for i in range(M):
        a,b = map(int, input().split())
        lst[a] = b
    postorder(1)
    print(f'#{tc} {lst[L]}')