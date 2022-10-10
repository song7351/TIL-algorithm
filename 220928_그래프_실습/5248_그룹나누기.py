"""
1~N명, M쌍의 종이
총 그룹의 개수는?
"""
test_case = int(input())

def f(arr, i):                      # 각 노드의 정점 찾기.
    global ans
    if arr[i] != i:                 # 각 노드의 정점 = 부모값이 본인자신
        return f(arr, arr[i])
    else:
        return i

def union_set(par, x,y):
    a = f(par, x)
    b = f(par, y)
    if a<b:
        par[b] = a
    else:
        par[a] = b

for tc in range(1, test_case + 1):
    N, M = map(int, input().split())
    grp = list(map(int,input().split()))
    par = [0]*(N+1)
    tmp = 0
    
    for i in range(N+1):    # Make-Set(x)
        par[i] = i
        
    for i in range(2*M):
        if not i%2:
            tmp = grp[i]
        else:               # Union(x,y)
            union_set(par, tmp, grp[i])

    for i in range(1,N+1):
        if par[i] != i:
            par[i] = f(par,i)

    ans = 0
    used_par = [0]*(N+1)
    for i in range(1,N+1):
        if used_par[par[i]] == 0:
            used_par[par[i]] = 1
            ans += 1
    #print(par)
    print(f'#{tc} {ans}')