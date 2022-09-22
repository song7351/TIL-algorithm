def f(i,k):
    if i == k:          # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(i,k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

p = [1,2,3]
f(0,len(p))
# f(0,10)