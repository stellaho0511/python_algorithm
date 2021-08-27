from collections import deque
import copy

n = int(input())
pic = [list(input()) for _ in range(n)]
cnt_n = 0
cnt_w = 0
pic_2 = copy.deepcopy(pic)
for i in range(n):
    for j in range(n):
        if pic_2[i][j] == 'G':
            pic_2[i][j] = 'R'
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bsf(i, j, color, picture, cnt):
    global cnt_n
    que = deque()
    que.append((i, j))
    picture[i][j] = 'o'
    cnt += 1
    while que:
        a, b = que.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and picture[x][y] == color:
                picture[x][y] = 'o'
                que.append((x, y))
    return cnt

for i in range(n):
    for j in range(n):
        if pic[i][j] != 'o':
            cnt_n = bsf(i, j, pic[i][j], pic, cnt_n)
        if pic_2[i][j] != 'o':
            cnt_w = bsf(i, j, pic_2[i][j], pic_2, cnt_w)


print(cnt_n, cnt_w)
