stackSize = 10
stack = [0] * stackSize
top = -1            #스택포인터: top의 위치

top += 1            #top = 0        top증가
stack[top] = 1      #stack[0] = 1   스택에 push

top += 1
stack[top] = 2

top -= 1
temp  = stack[top + 1]
print(temp)

temp = stack[top]
top -= 1
print(temp)

#----------------------------------------------------------

stack2 = []
stack2.append(1)
stack2.append(2)
print(stack2.pop())
print(stack2.pop())