# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수

def f(i, N):
    if i == N:      # 배열을 벗어남
        return
    else:           # 남은 원소가 있음
        print(A[i])
        f(i+1, N)   # 다음 원소로 이동

N = 3
A = [1,2,3]
f(0,N)
B = [0] * N
print(B)
