test_case = int(input())

def dfs(i,V):
    global minV,maxV,add,sub,mul,div
    if i == N:
        if V < minV:
            minV = V
        if V > maxV:
            maxV = V
    else:
        if add>0:
            add -= 1
            dfs(i+1, V+lst_num[i])
            add += 1
        if sub>0:
            sub -= 1
            dfs(i+1, V-lst_num[i])
            sub += 1
        if mul>0:
            mul -= 1
            dfs(i+1, V*lst_num[i])
            mul += 1
        if div>0:
            div -= 1
            dfs(i+1, int(V/lst_num[i]))
            div += 1

for tc in range(1, test_case + 1):
    N = int(input())
    add,sub,mul,div = map(int, input().split())
    lst_num = list(map(int, input().split()))

    maxV = -int(1e9)
    minV = int(1e9)

    dfs(1,lst_num[0])

    print(f'#{tc} {maxV-minV}')