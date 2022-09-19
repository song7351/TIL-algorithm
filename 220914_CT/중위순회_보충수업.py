import sys; sys.stdin = open('중위순회_input.txt')

def inorder(n):
    if n <= N:
        # 완전이진 트리이기 때문에 걍 2개만 사용함.
        inorder(2*n)
        print(tree[n], end='')
        inorder(2*n + 1)

test_case = 10

for tc in range(1, test_case + 1):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        tree[idx] = temp[1]

    print(f"#{tc}", end=' ')
    inorder(1)
    print()