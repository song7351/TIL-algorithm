"""
N명의 사람이 온다.
M초마다 K개를 생산한다.
손님은 0초부터 11111초사이에 들어온다.
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int,input().split()))
    last = max(lst)
    time = [0]*(last+1)
    bbang = 0
    for x in lst:
        time[x] += 1

    print(f'#{tc}',end=' ')
    for i in range(last+1):
        if i!=0 and i%M == 0:
            bbang += K

        if time[i] != 0:
            bbang -= time[i]
            if bbang < 0:
                print('Impossible')
                break
    else:
        print('Possible')



