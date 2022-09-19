"""
사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때
** 계산 결과값을 출력해라 **
총 10개의 테스트 케이스
첫 줄에는 정점의 개수 N(1≤N≤1000)
정점이 정수면 정점 번호, 양의 정수
정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호

중위...순회...?
"""
# import sys; sys.stdin = open('1232_사칙연산.txt')

def calcul(n):
    if n <= 1000+1:
        if par[n] in ['+','-','*','/']:     # 만약 부모가 사칙연산이라면 자식노드로 사칙연산하고 부모에 넣어라
            c1 = calcul(ch1[n])
            c2 = calcul(ch2[n])
            if par[n] == '+':
                par[n] = c1 + c2
            elif par[n] == '-':
                par[n] = c1 - c2
            elif par[n] == '*':
                par[n] = c1 * c2
            elif par[n] == '/':
                par[n] = c1 // c2
        return par[n]                       # 정수라면, 정수반환

test_case = 10

for tc in range(1, test_case + 1):
    N = int(input())
    par = [0] * (1000+1)                        # N은 최대 1000번까지있다.
    ch1 = [0] * (1000+1)
    ch2 = [0] * (1000+1)
    for _ in range(N):
        lst = list(input().split())
        if lst[1].isdigit():                    # 숫자면 그냥 값저장
             par[int(lst[0])] = int(lst[1])
        else:                                   # 문자면 자식이 무조건 2개!
            par[int(lst[0])] = lst[1]
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])

    ans = calcul(1)
    print(f'#{tc} {ans}')