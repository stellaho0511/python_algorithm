n, k = map(int, input().split())     #동전의 종류와 가치의 합
coin = [int(input()) for _ in [0]*n]
count = 0
for i in coin[::-1]:  # k를 만드는 데 필요한 동전의 개수의 최솟값 구하기
    count += (k // i)
    k %= coin[i]
    if k == 0:
        break
print(count)
