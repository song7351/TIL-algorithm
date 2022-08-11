'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다. N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 빨간색 영역과 파란색 영역의 외곽 길이를 구하는 프로그램을 만드시오. 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
'''
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]
    red = []
    d_red = 0
    blue = []
    d_blue = 0
    for _ in range(N):
        x1,y1,x2,y2,color = map(int, input().split())
        if color == 1:
            if not red:
                red.append([x1,y1,x2,y2])
                d_red += ((x2-x1+y2-y1+2)*2)
            else:
                for i in range(len(red)):
                    if (red[i][0] <= x1 <= red[i][2] and red[i][1] <= y1 <= red[i][3]) and (red[i][0] <= x2 <= red[i][2] and red[i][1] <= y2 <= red[i][3]):
                        pass
                    elif (red[i][0] <= x1 <= red[i][2] and red[i][1] <= y1 <= red[i][3]):
                        red.append([x1,y1,x2,y2])
                        d_red += ((red[i][0]-x2+red[i][1]-y2+2)*2)
                    elif (red[i][0] <= x2 <= red[i][2] and red[i][1] <= y2 <= red[i][3]):
                        red.append([x1,y1,x2,y2])
                        d_red += ((x1-red[i][1]+y1-red[i][3]+2)*2)
                    else:
                        red.append([x1,y1,x2,y2])
                        d_red += ((x2-x1+y2-y1+2)*2)
        else:
            if not blue:
                blue.append([x1,y1,x2,y2])
                d_blue += ((x2-x1+y2-y1+2)*2)
            else:
                for i in range(len(blue)):
                    if (blue[i][0] <= x1 <= blue[i][2] and blue[i][1] <= y1 <= blue[i][3]) and (blue[i][0] <= x2 <= blue[i][2] and blue[i][1] <= y2 <= blue[i][3]):
                        pass
                    elif (blue[i][0] <= x1 <= blue[i][2] and blue[i][1] <= y1 <= blue[i][3]):
                        blue.append([x1,y1,x2,y2])
                        d_blue += ((blue[i][0]-x2+blue[i][1]-y2+2)*2)
                    elif (blue[i][0] <= x2 <= blue[i][2] and blue[i][1] <= y2 <= blue[i][3]):
                        blue.append([x1,y1,x2,y2])
                        d_blue += ((x1-blue[i][1]+y1-blue[i][3]+2)*2)
                    else:
                        blue.append([x1,y1,x2,y2])
                        d_blue += ((x2-x1+y2-y1+2)*2)
        

    print(f'#{tc} {d_red+d_blue}')