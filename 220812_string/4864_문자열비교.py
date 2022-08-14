'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
ABC
ZZZZZABCZZZZZ
두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
ABC
ZZZZAZBCZZZZZ
문자열이 일치하지 않으므로 0을 출력.
'''
test_case = int(input())

for tc in range(1, test_case + 1):
    str1 = list(input())
    str2 = list(input())
    len1 = len(str1)
    len2 = len(str2)

    ans = 0
    #str2에서 str1길이 만큼 뺀 인덱스가 검색의 마지노선.
    for j in range(len2-len1+1):
        i = 0
        #시작점 찾기
        if str1[i] == str2[j]:
            cnt = 1
            # str1과 str2가 같은지 검색
            for k in range(1, len1):
                if str1[i+k] == str2[j+k]:
                    cnt += 1
                else:
                    break
            # 같을때 마다 +1해서 그 결과 len1과 같다면 break
            if cnt == len1:
                ans = 1
                break


    print(f"#{tc} {ans}")