"""
중위순회: 왼쪽자식 부모 오른쪽자식
정점의 총 수 N(1≤N≤100)
정점 정보는 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호 순서
"""
def in_order(n):
    global word
    if n:
        in_order(ch1[n])
        word += par_chr[n]
        in_order(ch2[n])

test_case = 10

for tc in range(1, test_case+1):
    N = int(input())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    par_chr = [''] * (N+1)
    for i in range(N):
        lst = list(input().split())
        p = int(lst[0])
        if len(lst) > 2:
            ch1[p] = int(lst[2])    # 왼쪽자식
        if len(lst) > 3:
            ch2[p] = int(lst[3])    # 오른쪽 자식
        par_chr[p] = lst[1]         # 문자열

    word = ''                       # 출력할 문자열
    in_order(1)                     # 최초시작은 1부터.
    print(f'#{tc} {word}')