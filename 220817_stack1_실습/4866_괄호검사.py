"""
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.

정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.

print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
"""

test_case = int(input())

for tc in range(1, test_case+1):
    word = list(input())
    N = len(word)
    gwalho = []
    flag = 0
    for i in range(N):
        if word[i] == '{' or word[i] == '(':        # 문자열이 여는괄호라면, gwalho리스트에 추가해라.
            gwalho.append(word[i])

        if word[i] == '}' or word[i] == ')':                # 문자열이 닫는괄호라면,
            if not len(gwalho):                             # gwalho리스트가 없다면 error
                flag = 1
                break
            elif word[i] == '}' and gwalho[-1] == '{':      # 짝이 맞는다면 pop
                gwalho.pop()
            elif word[i] == ')' and gwalho[-1] == '(':      # 짝이 맞는다면 pop
                gwalho.pop()
            else:                                           # 짝이 틀리다면 error
                flag = 1
                break

    if flag == 1 or len(gwalho) != 0:                       # gwalho리스트가 없거나 여는괄호가 남아있다면 error
        ans = 0
    else:
        ans = 1
    print(f"#{tc} {ans}")