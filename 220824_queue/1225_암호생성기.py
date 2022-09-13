"""
8자리 암호
1사이클: i자리부터 i씩 감소후 뒤로 이동.
사이클 반복하다가 0이하가된다면 해당 리스트 고정
즉, 모든 비밀번호는 a b c d e f g 0
"""

for _ in range(10):
    test_case = int(input())
    amho = list(map(int, input().split()))      # 8자리 입력받음.

    while amho[-1] != 0:                        # 끝자리가 0나올때까지 반복
        diff = 1
        num = amho.pop(0) - diff
        if num < 0:
            num = 0
        amho.append(num)
        diff += 1
        if diff == 6:
            diff = 1

    amho = map(str, amho)
    print(f"#{test_case} {' '.join(amho)}")

