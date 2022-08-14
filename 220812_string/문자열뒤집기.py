"""
문자열 뒤집기
방법 1. 인덱스 슬라이싱
        s[::-1]

방법 2. 리스트 reverse
        s.reverse()
        ''.join(s)

방법 3. 리스트 역순으로 불러서 빈문자열에 더한다
"""

# 방법 4. 투포인터 왼쪽, 오른쪽 정렬
text = list(input())

left = 0
right = len(text) - 1
while left < right:
    text[left], text[right] = text[right], text[left]
    left += 1
    right -= 1

print(''.join(text))