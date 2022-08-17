#memo를 위한 배열을 할당하고, 모두 0으로 초기화
#memo[0]을 0으로 memo[1]은 1로 초기화

def fibo1(n):
    if n>=2 and len(memo) <= n :
        memo.append(fibo1(n-1) + fibo1(n-2))     # append보다 속도를 더 빠르게 하고싶다면
    return memo[n]                               # 사전에 배열을 만들어놔라


memo = [0,1]
print(fibo1(6))
print(memo)