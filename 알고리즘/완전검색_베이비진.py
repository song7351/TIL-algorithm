def f(i,n):
    if i == n:
        """
        여기서 6자리를 비교한다. 
        """
        pass
    else:
        for j in range(0):
            if used[j] == 0:
                used[j] = 1
                p[j] = a[i]
                f(i+1,n)
                used[j] = 0

N = 6
a = [i for i in range(1, N+1)]
p = [0]* N
used = [0]* N
f(0,N)