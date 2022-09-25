"""
num2 = 2진수를 10진수로 바꾼것
2진수:
각 자리마다 검사시작
각 자리가 1이면, 2**N-1-i을 빼줌
각 자리가 0이면, 2**N-1-i을 더해줌

3진수:
각 자리마다 검사시작
각 자리가 1이면, 3**N-1-i 을 더해주고 뺌
각 자리가 0이면, 3**N-1-i 을 더해주고 2번더해줌
각 자리가 2이면, 3**N-1-i 을 빼주고 2번빼줌
"""

test_case = int(input())

for tc in range(1, test_case + 1):
    bina = list(input())
    trit = list(input())
    num2 = int(''.join(bina),2)
    num3 = int(''.join(trit),3)

    lst2 = []
    lst3 = []
    for i in range(len(bina)):
        if bina[i] == '0':
            lst2.append(num2 + 2**(len(bina)-1-i))
        elif bina[i] == '1':
            lst2.append(num2 - 2**(len(bina)-1-i))

    for i in range(len(trit)):
        if trit[i] == '0':
            lst3.append(num3 + 3**(len(trit)-1-i))
            lst3.append(num3 + 2*(3**(len(trit)-1-i)))
        elif trit[i] == '1':
            lst3.append(num3 + 3**(len(trit)-1-i))
            lst3.append(num3 - 3**(len(trit)-1-i))
        elif trit[i] == '2':
            lst3.append(num3 - 3**(len(trit)-1-i))
            lst3.append(num3 - 2*(3**(len(trit)-1-i)))

    intersection = list(set(lst2)&set(lst3))

    print(f'#{tc} {intersection[0]}')