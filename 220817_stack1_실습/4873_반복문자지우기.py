"""
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50

다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.
"""

test_case = int(input())

for tc in range(1, test_case+1):
    word = list(input())
    start = 0                               # 시작 인덱스
    while True:
        if word[start] == word[start+1]:    # 연달아서 같다면, 두개다 빼고 처음부터 다시 검색해라
            word.pop(start)
            word.pop(start)
            start = 0
        else:
            start += 1
        if start == len(word)-1:
            break

    print(f"#{tc} {len(word)}")