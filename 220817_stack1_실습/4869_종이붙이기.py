"""
가로x세로 길이가 10x20, 20x20인 직사각형 종이만 존재한다.

교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수

"""
"""
원리
1. 길이가 10일때는 방법은 1가지
2. 길이가 20일때는 방법은 3가지
3. 길이가 30이상일 경우,
    3-1. 이전 인덱스(i-1)에 20*10 을 추가하는 방법 = arr[i-1] 개
    3-2. 이전전 인덱스(i-2)에 20*20 혹은 10*20 10*20 을 추가하는 방법 = arr[i-2]*2 개
    3-3. arr[i] = arr[i-1] + arr[i-2]*2 
"""
paper = []

for i in range(30):
    if i == 0:
        paper.append(1)
    if i == 1:
        paper.append(3)
    if i > 1:
        paper.append(paper[i-1]+paper[i-2]*2)

test_case = int(input())

for tc in range(1, test_case+1):
    num = int(input())
    idx = (num//10) - 1
    print(f"#{tc} {paper[idx]}")