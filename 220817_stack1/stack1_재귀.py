#재귀함수 특징: 목표치(종료지점)가 있음.

def f(i, N):
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)