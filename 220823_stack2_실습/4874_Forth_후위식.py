"""
후위표기법을 주어준다.

단, .을 만나면 결과값을 출력해라.

"""

test_case = int(input())

for tc in range(1, test_case + 1):
    lst = list(input().split())
    yeonsanja = ['+', '*', '/', '-']
    num = []
    n1 = 0
    n2 = 0
    ans = 0
    for i in lst:
        if i == '.':
            break

        if i not in yeonsanja:                      # 숫자라면 num에 추가
            num.append(int(i))
        elif i in yeonsanja and len(num) >= 2:      # 연산자일때, num의 길이가 2개이상이여야함.
            n1 = num.pop()
            n2 = num.pop()
            if i == '+':
                num.append( n2 + n1 )
            elif i == '*':
                num.append( n2 * n1 )
            elif i == '-':
                num.append( n2 - n1 )
            elif i == '/':
                num.append( n2 // n1 )
        else:                                       # 아닐경우에는 error처리.
            ans = 'error'
            break

    if ans != 'error' and len(num) == 1:
        print(f'#{tc} {num[0]}')
    else:
        print(f'#{tc} error')