from collections import deque
import copy

n = int(input())
pic = [list(input()) for _ in range(n)]
cnt_n = 0
cnt_w = 0
pic_2 = copy.deepcopy(pic)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def normal(i, j, color):   # 일반 사람의 경우의 한 구역
    global cnt_n
    que = deque()
    que.append((i, j))
    pic[i][j] = 'o'
    cnt_n += 1
    while que:    # 해당 구역에 포함되는 칸 check하기
        a, b = que.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and pic[x][y] == color:
                pic[x][y] = 'o'
                que.append((x, y))
def color_weakness(i, j, color):     # 적록색약이 있는 경우 구역
    global cnt_w
    que = deque()
    que.append((i, j))
    pic_2[i][j] = 'o'
    cnt_w += 1

    while que:
        a, b = que.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if color == 'B':
                    if pic_2[x][y] == color:
                        pic_2[x][y] = 'o'
                        que.append((x, y))

                elif color == 'R' or color == 'G':
                    if pic_2[x][y] == 'R' or pic_2[x][y] == 'G':
                        pic_2[x][y] = 'o'
                        que.append((x, y))

for i in range(n):
    for j in range(n):
        if pic[i][j] != 'o':
            normal(i, j, pic[i][j])
        if pic_2[i][j] != 'o':
            color_weakness(i, j, pic_2[i][j])

print(cnt_n, cnt_w)
