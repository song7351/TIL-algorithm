"""
 1번부터 N번
 처음엔 0
  Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
  ·  i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N,Q= map(int,input().split())
    box = [0]*1001
    for i in range(1,Q+1):
        L,R = map(int, input().split())
        for j in range(L,R+1):
            box[j] = i

    print(f'#{tc}', end=" ")
    for i in range(1,N+1):
        print(box[i], end=" ")
    print()