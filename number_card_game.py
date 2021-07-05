n, m = map(int, input().split())
result = 0

# 한 줄 씩 입력 받기
for i in range(n):
    data = list(map(int, input().split()))
    min_n = min(data)
    result = max(result, min_n)    # 가장 작을 수 중 큰 수 찾기
print(result)
