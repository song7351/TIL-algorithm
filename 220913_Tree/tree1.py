"""
13 V 마지막 정점, 노드개수 ...
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
def pre(n):
    global cnt
    if n:
        cnt += 1
        print(n, end=' ')
        pre(ch1[n])
        pre(ch2[n])

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:     # 부모가 없다면? root
            return i

V = int(input())
arr = list(map(int, input().split()))
E = V - 1 # 간선수
ch1 = [0] * (V+1)   # 부모인덱스에 자식1
ch2 = [0] * (V+1)   # 부모인덱스에 자식2
par = [0] * (V+1)   # 자식인덱스에 부모번호 저장

# 부모 인덱스, 자식저장
for i in range(E):
    p, c = arr[i*2], arr[i*2 + 1]   # 부모, 자식
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

# 만약 3으로 시작하는 트리만 보고싶다.
cnt = 0
pre(3)
print()
print(f"cnt = {cnt}")

# root = find_root(V)
# pre(root)
# print()
# print(root)