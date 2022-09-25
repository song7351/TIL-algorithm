"""
2진수중 한자리만 틀렸다.
3진수중 한자리만 틀렸다.

그래서 둘다 고쳤을때 2진수 값 == 3진수 값

1줄: 테스트케이스
2줄: 2진수
3줄: 3진수
"""

test_case = int(input())

def f2(i):
    word = ''
    if bina[i] == '0':
        word = '1'
    else:
        word = '0'
    num = bina[:i] + [word] + bina[i+1:]
    return int(''.join(num), 2)

for tc in range(1, test_case + 1):
    bina = list(input())
    trit = list(input())
    ans = 0
    for i in range(len(bina)):
        num2 = f2(i)
        for j in range(len(trit)):
            for k in range(3):
                if trit[j] == str(k):
                    continue
                else:
                    word = trit[:j] + [str(k)] + trit[j+1:]
                    num3 = int(''.join(word),3)
                    if num3 == num2:
                        ans = num3
                        break
            if ans:
                break
        if ans:
            break

    print(f'#{tc} {ans}')