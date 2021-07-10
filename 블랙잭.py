n, m = map(int, input().split())
c = list(map(int, input().split()))
max_n = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
             s = c[i] + c[j] + c[k]
             if s <= m and max(s, max_n):
                max_n = max(max_n, s)
print(max_n)
