def star(n):
    global stars
    if n == 3:
        stars[0][:3] = stars[2][:3] = ['*'] * 3
        stars[1][:3] = ['*', ' ', '*']
        return

    div3 = n // 3
    star(div3)

    for i in range(3):   # 9개 칸
        for j in range(3):
            if i == 1 and j ==1:
                continue
            for k in range(div3): # 각 칸
                stars[i*div3 + k][j * div3 : (j-1) * div3] = stars[k][:div3]


N = int(input())
stars = [[' ' for i in range(N)] for i in range(N) ]
star(N)
for i in range(N):
    for j in range(N):
        print(stars[i][j], end = '')
    print()
