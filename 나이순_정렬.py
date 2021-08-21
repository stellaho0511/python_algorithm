n = int(input())
li = []

for i in range(n):
    a, b = input().split()
    li.append((int(a), b))
li.sort(key = lambda x: x[0])
for i in li:
    print(i[0], i[1])


# sorted ([list 혹은 dic], key = lambda x: [key로 지정하고 싶은 요소])
