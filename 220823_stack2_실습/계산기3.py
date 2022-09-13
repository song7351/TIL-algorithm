"""
후위 표기식으로 바꾸고 계산해라
"""

test_case = 10

for tc in range(1, test_case + 1):
    N = int(input())
    lst = list(input())

    yeonsanja = {'(': 4, '*': 3, '+': 2, ')': 0}

    stack = []
    postfix = []
    # 후위표기법
    for i in lst:
        if i not in yeonsanja:
            postfix.append(int(i))
        else:
            if not stack:
                stack.append(i)
            elif i == ')':                  # 닫는 괄호가 나온다면 여는 괄호가 나올때까지 append, pop
                x = stack.pop()
                while x != '(':
                    postfix.append(x)
                    x = stack.pop()
            elif stack[-1] == '(':          # stack의 마지막이 여는 괄호면 그냥 append
                stack.append(i)
            elif yeonsanja[i] <= yeonsanja[stack[-1]]:  # 우선 순위가 같거나 밀린다면, pop append
                while stack and yeonsanja[i] <= yeonsanja[stack[-1]] and stack[-1] != '(':  #단, 여는괄호가 나오면 그만해라.
                    postfix.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)

    while stack:
        postfix.append(stack.pop())

    # 후위표기법 계산
    num = []
    n1 = 0
    n2 = 0
    for i in postfix:
        if i not in yeonsanja:
            num.append(i)
        else:
            if i == '*':
                n1 = num.pop()
                n2 = num.pop()
                num.append(n1 * n2)
            elif i == '+':
                n1 = num.pop()
                n2 = num.pop()
                num.append(n1 + n2)

    print(f'#{tc} {num[0]}')