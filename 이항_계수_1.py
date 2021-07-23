from math import factorial

def comb(n,k):         # 재귀 함수
    if  k == 0 or n == k:
        return 1
    return comb(n-1, k-1) + comb(n-1, k)

n, k = map(int, input().split())    # 첫번째 방법
print(comb(n, k))
b = factorial(n) // (factorial(k) * factorial(n-k))  # 두번째 방법
print(b)
