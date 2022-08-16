"""
어떤 문자열 A를 타이핑하려고 한다.

그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.

여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.

이미 타이핑 한 문자를 지우는 것은 불가능하다.

예를 들어 A=”asakusa”, B=”sa”일 때, 다음 그림과 같이 B를 두 번 사용하면 5번 만에 A를 타이핑 할 수 있다.

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스마다 첫 번째 줄에 두 문자열 A, B가 주어진다. A의 길이는 1이상 10,000이하, B의 길이는 1이상 100이하이다.
"""
'''
주의해야할 반례
1. aaasakuaaa aa

2. asakua aaaaaaaa
'''
test_case = int(input())

for tc in range(1, test_case + 1):
    str1, str2 = input().split()
    str1 = list(str1)
    str2 = list(str2)

    cnt = 0

    if len(str1) < len(str2):
        print(f'#{tc} {len(str1)}')
    else:
        # 검색할 범위는 str2의 길이만큼이다.
        left = 0
        right = left + len(str2)
        while left < len(str1) - len(str2) + 1:
            new_str1 = str1[left:right]
            # 만약 범위의 값이 같다면 cnt += 1해주고 끝인덱스를 다음 검색 시작인덱스로 바꿔줌
            if str2 == new_str1:
                cnt += 1
                left = right
                right = left + len(str2)
            else:
                left += 1
                right += 1

        # 원래 총 타이핑 길이는 str1의 길이
        # 중복단어(str2)는 길이가 1로 변하므로 그 차이(len(str2)-1)의 반복(cnt)만큼
        # st1의 길이에서 빼줘야함.
        ans = len(str1) - ((len(str2)-1)*cnt)

        print(f'#{tc} {ans}')