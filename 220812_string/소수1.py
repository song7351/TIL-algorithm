def isPrime(n):
    if n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        i = 2
        while i ** i <= n:
            if n % i == 0:
                return 0
            i += 1
        return 1
