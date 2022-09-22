test_case = int(input())

def check(arr):
    if sum(arr) >= 3:
        for i in range(8):
            if arr[i]>0 and arr[i+1]>0 and arr[i+2]>0:
                return 1
            if arr[i]>=3 or arr[i+1]>=3 or arr[i+2]>=3:
                return 1
    return 3
for tc in range(1, test_case + 1):
    card = list(map(int,input().split()))
    a = [0] * 10
    b = [0] * 10
    ans = 3
    for i in range(12):
        if i%2 ==0:
            a[card[i]] += 1
            ans = check(a)
        else:
            b[card[i]] += 1
            ans = check(b)

        if ans != 3:
            if i%2 ==0:
                print(f"#{tc} {1}")
            else:
                print(f"#{tc} {2}")
            break
    else:
        print(f"#{tc} 0")
