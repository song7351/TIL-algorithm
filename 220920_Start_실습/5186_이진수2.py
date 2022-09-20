"""
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다.
예를 들어 0.625를 이진 수로 바꾸면 0.101
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N
"""
test_case = int(input())

for tc in range(1, test_case + 1):
    N = float(input())                  # 실수로 받는다.
    binary = ''
    f_num = N*2                         # 2씩 곱해서 정수부분을 취한다.
    while  f_num != 1.0:
        if f_num >= 1:
            f_num -= float(1)
            binary += '1'
        else:
            binary += '0'
        f_num *= 2
        if len(binary) >= 12:
            binary = 'overflow'
            break
    if f_num == 1.0:
        binary += '1'
    print(f'#{tc} {binary}')