n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k
count += m % (k + 1)

result = count * first       # 가장 큰 수 더하기
result += (m - count) * second      # 두번째로 큰 수 더하기
print(result)
