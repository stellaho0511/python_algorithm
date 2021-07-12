N = int(input())
time = []

for i in range(N):      # 회의 시작 시간과 끝나는 시간 입력
    a, b = map(int, input().split())
    time.append([a, b])
time.sort(key=lambda x: (x[1], x[0]))   # 끝나는 시간, 시작 시간으로 정렬
count = 0
end = 0
for i, j in time:   # 회의 수 세기
    if end <= i:      # 회의 끝나는 시간이 시작 시간 보다 작을 때 +1
        count += 1
        end = j
print(count)
