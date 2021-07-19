n = int(input())
w_h = []
for i in range(n):
    w_h.append(input().split())     # or a.append((weight, height))
# 앞에 몇 명이 있는가가 중요
for i in range(len(w_h)):
    cnt = 1
    for j in range(len(w_h)):
        if(w_h[i][0] < w_h[j][0] and w_h[i][1] < w_h[j][1]):
            cnt += 1
    print(cnt, end = ' ')
print(s)
