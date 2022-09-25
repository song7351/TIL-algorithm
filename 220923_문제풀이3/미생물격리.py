"""
// 총 테스트케이스 개수 T=10
// 테스트 케이스 1,     N=7, M=2, K=9
// 세로위치(1), 가로위치(1), 미생물 수(7), 이동
1시간이 지난다?

-> 해당위치의 군집이 해당 방향으로 이동

-> 이동후, 군집이 여러개인가? -> 합쳐줌
-> 테두리에 위치한가? -> 절반감소, 반대방향

"""
test_case = int(input())

for tc in range(1, test_case + 1):
    # 한변의 크기는 N, 제한시간M, 군집의 수K
    N,M,K = map(int,input().split())

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    # 군집
    gunjib = [0]*K
    for i in range(K):
        # 세로 위치, 가로 위치, 미생물 수, 이동 방향
        x,y,c,d = map(int, input().split())
        gunjib[i] = [x,y,c,d]

    while M:
        M -= 1
        # 이동하세요.
        for i in range(len(gunjib)):
            ni = gunjib[i][0] + di[gunjib[i][3]]
            nj = gunjib[i][1] + dj[gunjib[i][3]]
            c,d = gunjib[i][2], gunjib[i][3]
            if ni in [0,N-1] or nj [0,N-1]:
                d = (d+2)%4
                c = c//2
                if c == 0:
                    gunjib[i] == 0
                else:
                    gunjib[i] = [ni,nj,c,d]
            else:
                gunjib[i] = [ni,nj,c,d]

        # 같은 위치를 공유하는 군집들을 찾아라
        board = [[0]*N for _ in range(N)]
        for i in range(len(gunjib)):
            if gunjib[i] != 0:
                x2,y2,c2,d2 = gunjib[i][0],gunjib[i][1],gunjib[i][2],gunjib[i][3]
                if board[x2][y2] == 0:
                    board[x2][y2] = [[c2, d]]
                else:
                    board[x2][y2].append([c2, d2])

        gunjib = []
        for i in range(N):
            for j in range(N):
                if len(board[i][j]) == 1:
                    gunjib.append(board[i][j][0])
                elif len(board[i][j]) > 1:
                    max_d, max_s, max_k = 0,0,0
                    for k in range(len(board[i][j])):
                        max_s += board[i][j][k][2]
                        if board[i][j][k][2] > max_k:
                            max_k = board[i][j][k][2]
                            max_d = board[i][j][k][3]
                    gunjib.append([board[i][j][0][0],board[i][j][0][1],max_s,max_d])

    ans = 0
    for i in gunjib:
        ans += i[2]
    print(f'#{tc} {ans}')