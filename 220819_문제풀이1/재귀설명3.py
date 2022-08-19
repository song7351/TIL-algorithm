def f(i,N):
    if i == N:
        print(bit)
        return
    else:
        bit[i] = 0
        f(i+1, N)
        bit[i] = 1
        f(i+1, N)


bit = [0] * 3
f(0,3)