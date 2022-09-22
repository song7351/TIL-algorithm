"""
부분집합의 합
10개의 정수 집합에 대한 모든 부분 집합 중
원소의 합이 0이 되는 부분집합을 모두 출력하세요.
"""
from itertools import combinations
from itertools import permutations
from itertools import product


N = [-1,3,-9,6,7,-6,1]
items = [[1,2,3], ['a','b'], ['!','@','#']]
"""
lst = [[]]
for i in N:
    for j in range(len(lst)):
        lst.append(lst[j] + [i])
        
lst.pop(0)

for i in lst:
    if not sum(i):
        print(i)
"""

combin_lst = list(combinations(N, 2))
permute_lst = list(permutations(N, 2))
pro_lst = list(product(*items))

print(combin_lst)
print(permute_lst)
print(pro_lst)
