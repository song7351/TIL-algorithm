
test_case = int(input())

for tc in range(1,test_case+1):
    gwalho = input()
    stack = []
    answer = 1

    for x in gwalho:
        if x == '(':
            stack.append('(')
        elif x == ')':
            if len(stack) == 0:     # 여는 괄호가 모자란 경우
                answer = 0
                break
            else:
                stack.pop()         # 짝이 맞다면, 여는 괄호 제고

    if len(stack):                  # 전부 검사했는데 여는 괄호가 남는경우
        answer = 0
    print(f"#{tc} {answer}")