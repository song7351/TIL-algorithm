'''
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c' # 'abc'
s6 = s1[::]

print(s1 == s5) # True
print(s1 is s5) # False -> id값이 다름.
                # s1 = 'abc' s5 = 'ab' + 'c'
print(s1 is s2) # True
'''

'''
문자열이 같으면 0 리턴
사전 순서상 앞서면 -1 아니라면 1
'''
'''
방법 1. 길이비교로 가능. -> 길이가 짧으면 우선순위 Up
        길이가 같다면 글자별로 비교.

def dict_sort(s1, s2):
    s1len = len(s1)
    s2len = len(s2)
    i = 0
    #둘 다 인덱스가 존재하는 상황
    while i  < s1len and i < s2len:
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])  #다른 글자
        i += 1        
    # 내용이 같은 경우, 한쪽이 짧음
    if s1len == s2len:
        return 0
    else:
        return s1len - s2len

'''
a = 'abc'
b = 'def'
c = 'de'
d = 'ABC'
print(a < b)    # True
print(a > b)    # False
print(b < c)    # False
print(b > c)    # True
print(a < d)    # False
print(a > d)    # True
# 결론: 알파벳 순서가 더 빠르다면 더 작다
# 결론2: 대문자가 소문자보다 더 작다.



