"""
1줄: 테스트케이스의 수 T가 주어진다. 1<=T<=50

2줄: 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100

16진수 A부터 F는 대문자로 표시된다.

2진수 : 0b
8진수 : 0o (영어 소문자 O)
16진수 : 0x

# 10진수 -> 진수 변환
binary = bin(number)
octal = oct(number)
hexa = hex(number)

# 진수 -> 10진수 변환
binary = int('0b0111011', 2)
octal = int('0o21562', 8)
hexa = int('0xFA21BC', 16)

"""

test_case = int(input())

for tc in range(1, test_case + 1):
    N,M = input().split()
    M = '0x'+M                  # 16진수로 표시
    num = int(M, 16)            # 16진수 -> 10진수 변환
    binary = bin(num)           # 10진수 -> 2진수 변환
    binary = binary[2:]         # 2진수 변환시 앞에 2진수임을 표시하는 0b가 붙음
    while len(binary)%4 != 0:   # 자리수가 4의 배수가 될때까지 앞에 0을 추가
        binary = '0' + binary
    print(f'#{tc} {binary}')