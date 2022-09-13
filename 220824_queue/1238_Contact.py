def f(start):
    novisit_list = [start]
    dept_list = [0] * 101
    dept_list[start] = 1
    while novisit_list:
        node = novisit_list.pop(0)
        if dept_list[node] != 0:
            if node in graph:
                novisit_list.extend(graph[node])
                for x in graph[node]:
                    if dept_list[x] == 0:
                        dept_list[x] = dept_list[node] + 1

    print(dept_list)
    return 0

test_case = 10

for tc in range(1, test_case + 1):
    N, S = map(int, input().split())
    contact = list(map(int, input().split()))
    graph = {}
    for i in range(N//2):
        n1 = contact[2*i]
        n2 = contact[2*i+1]

        if n1 not in graph:
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

    ans = f(S)
    print(f'#{tc} ')