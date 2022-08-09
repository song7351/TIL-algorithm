'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

입력
첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
1<=T<=10, 10<=N<=1000
'''

test_case = int(input())

for tc in range(1,test_case+1):
    N = int(input())
    num_list = list(map(int, input()))
    max_cnt = 0
    cnt = 0
    for i in range(N-1):
        if num_list[i] == num_list[i+1] == 1: # 연속된 1이 나온다면 cnt +1
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        if num_list[i] != num_list[i+1]:      # 두개 연속해서 다르다면 길이는 1이다.
            cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt

    print(f"#{tc} {max_cnt}")