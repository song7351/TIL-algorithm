"""

"""

test_case = int(input())

for tc in range(1, test_case + 1):
    d,m1,m3,y = map(int, input().split())
    year = list(map(int, input().split()))
    cost = [0]*14
    for i in range(12):
        if d*year[i] < m1:
            cost[i] = d*year[i]
        else:
            cost[i] = m1
            
    ans = y
    if sum(cost) < ans:
        ans = sum(cost)

    for i in range(12):
        k = i
        cost2 = cost[:]
        while k < 12:
            if cost2[k] == 0:
                k += 1
                continue
            else:
                if cost2[k] + cost2[k+1] + cost2[k+2] > m3:
                    cost2[k], cost2[k + 1], cost2[k + 2] = m3,0,0
                    k += 3
                else:
                    k += 1

        if sum(cost2) < ans:
            ans = sum(cost2)

    print(f'#{tc} {ans}')