"""
16진수 -> 2진수(각 4자리)로 변환하여 삽입
뒤부터 1을 찾으면 뒤부터 비율을 계산해봅시다.
"""
import sys; sys.stdin = open('1242_암호스캔.txt')

def chg_bin():
    for i in range(N):
        for j in range(M):
            bin_num = bin(int(arr[i][j],16))[2:]
            while len(bin_num) % 4 != 0:
                bin_num = '0' + bin_num
            arr2[i].extend(bin_num)
# 비율 역순
secret_code = [
    [1,1,2,3],
    [1,2,2,2],
    [2,2,1,2],
    [1,1,4,1],
    [2,3,1,1],
    [1,3,2,1],
    [4,1,1,1],
    [2,1,3,1],
    [3,1,2,1],
    [2,1,1,3]
]
test_case = int(input())

for tc in range(1, test_case + 1):

    N,M = map(int, input().split())
    arr = [list(map(str,input())) for _ in range(N)]    # 전체 2차원 배열(16진수)
    #if tc != 9:
    #    continue
    #print(N, M)
    arr2= [[] for _ in range(N)]                        # 전체 2차원 배열(2진수)
    chg_bin()                                           # 16진수 -> 2진수
    # print(arr2)
    M = 4*M                                             # 전체 길이를 2진수로 변환과정에서 4배로 증가.
    # 여태 나왔던 수.
    num_list = []
    ans = 0
    #for i in range(N):
    for i in range(57,N):
        flag = 0                                        # flag = 0 첫번째 1을 확인하는 용도
        one_cnt = 0                                         # 1카운트하는 용도
        zero_cnt = 0                                        # 0을 카운트하는 용도
        code = []                                       # 비율 역순으로 확인하기 위한 용도
        # 전체 8자리수(역순)
        num1 = []
        # 전체 8자리수(정순)
        num2 = []
        # 최초의 배율
        z = 0
        #for j in range(M-1,-1,-1):                              # 각 행의 뒤부터 검색한다.
        for j in range(448,-1,-1):                              # 각 행의 뒤부터 검색한다.
            xxxx = arr2[i][j]
            if flag == 0 and arr2[i][j] == '1':                    # 만약 첫번째 1일 경우부터 확인해줍시다.
                flag = 1
                one_cnt = 1
            elif flag == 1 and arr2[i][j] == '1':
                if zero_cnt != 0:
                    code.append(zero_cnt)
                    zero_cnt = 0
                one_cnt += 1
            elif flag == 1 and arr2[i][j] == '0':
                if one_cnt != 0:
                    code.append(one_cnt)
                    one_cnt = 0
                zero_cnt += 1
                if len(code) == 3 and (sum(code)+zero_cnt) % 7 == 0 and len(num1) == 7:
                    code.append(zero_cnt)

            # 만약에 코드가 4자리가 된다면,
            if len(code) == 4:
                if z == 0:
                    z = min(code)
                for k in range(4):
                    code[k] = code[k]//z

                for k in range(10):
                    if secret_code[k] == code:
                        num1.append(k)
                        break
                code = []
                one_cnt, zero_cnt, flag = 1,0,1

            # 만약에 num1이 8자리가 된다면,
            if len(num1) == 8:
                num2 = num1[::-1]
                num1 = []
                z = 0
                if num2 not in num_list:
                    print(num2)
                    num_list.append(num2)
                    if ((num2[0] + num2[2] + num2[4] + num2[6])*3 + num2[1] + num2[3] + num2[5] + num2[7]) % 10 == 0:
                        ans += sum(num2)
                        num2 = []
                        one_cnt,flag = 0,0

    print(f'#{tc} {ans}')