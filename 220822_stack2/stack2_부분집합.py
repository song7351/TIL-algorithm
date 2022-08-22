def f(i,N):
    if i == N:
        #print(bit)

        #for i in range(N):
        #    if bit[i]:
        #        print(A[i], end=" ")
        #print()

        global answer
        s = 0
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == 10:
            answer += 1
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1,2,4,5,6,7,8,9,10]
bit = [0] * 10
answer = 0

f(0, 9)
print(answer)