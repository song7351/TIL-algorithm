"""
문자열 계산식이 주어질 때, 후위 표기식으로 바꿔서 계산해라
연산자 = +, * 만 주어진다.
피연산자는 0 ~ 9만 주어진다.
9
3+4+5*6+7
"""

test_case = 10
for tc in range(1, test_case+1):
    N= int(input())
    gyesangi = list(input())

    yeonsanja = {'*': 3, '+': 2}        # 연산자 우선순위
    lst = []
    stack = []

    # 후위 연산자표기
    for x in gyesangi:
        if x not in yeonsanja:          # 연산자가 아니라면, 숫자라면 lst에 넣는다.
            lst.append(x)
        else:
            if not stack:               # 연산자이지만, stack이 비어있다면 집어 넣는다.
                stack.append(x)
            else:
                if yeonsanja[x] <= yeonsanja[stack[-1]]:                    # 우선순위가 stack의 마지막보다 작거나 같다면.
                    while stack and yeonsanja[x] <= yeonsanja[stack[-1]]:   # stack이 비거나 작거나 같을때까지 pop해서 lst에 추가한다.
                        lst.append(stack.pop())
                    stack.append(x)
                else:
                    stack.append(x)
    while stack:
        lst.append(stack.pop())
    # print(''.join(lst))

    # 후위 연산자 계산
    num = []
    n1 = 0
    n2 = 0
    for x in lst:
        if x not in yeonsanja:
            num.append(int(x))
        else:
            if x == '*':
                n1 = num.pop()
                n2 = num.pop()
                num.append(n1 * n2)
            elif x == '+':
                n1 = num.pop()
                n2 = num.pop()
                num.append(n1 + n2)

    print(f"#{tc} {num[0]}")
