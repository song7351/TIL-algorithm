infix = '2+3*4/5'

postfix = ''

op = ['+','-','*','/']

stack = [0] * 10
top = -1

for x in infix:
    if x not in op:
        postfix += x        # 숫자 push
        print(postfix)
    else:
        top += 1            # 사직연산 push
        stack[top] = x
        print(stack)

print('--------------------------------')
while top > -1:
    postfix += stack[top]   # pop
    top -= 1
    print(postfix)