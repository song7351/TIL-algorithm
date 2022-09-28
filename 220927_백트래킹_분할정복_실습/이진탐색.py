test_case = int(input())

def b_search(start, end, target,direction):
    global ans
    if start <= end:
        middle = (start+end)//2
        if N_lst[middle] == target:
            ans += 1
            return
        elif N_lst[middle] > target:
            if direction != 2:
                direction = 2
                b_search(start, middle-1, target,direction)
            else:
                return
        else:
            if direction != 1:
                direction = 1
                b_search(middle+1, end, target,direction)
            else:
                return

for tc in range(1, test_case + 1):
    N,M = map(int, input().split())
    N_lst = sorted(list(map(int,input().split())))
    M_lst = list(map(int, input().split()))

    ans = 0
    for x in M_lst:
        b_search(0,N-1,x,0)

    print(f'#{tc} {ans}')