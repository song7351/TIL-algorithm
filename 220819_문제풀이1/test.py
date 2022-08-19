"""
첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다.

N은 온도 수열의 길이 2<= N <= 100,000
K는 연속된 수열의 길이   1<K<N

모든 온도는 -100 ~ 100

"""

N, K = map(int, input().split())
num_list = list(map(int, input().split()))

max_sum = -100 * 100000
test_sum = 0
for i in range(K):
    test_sum += num_list[i]

if test_sum > max_sum:
    max_sum = test_sum

for i in range(K, N):
    test_sum += num_list[i] - num_list[i-K]
    if test_sum > max_sum:
        max_sum = test_sum

print(max_sum)