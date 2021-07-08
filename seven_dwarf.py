num = [int(input()) for _ in range(9)]     # 번호 아홉개 받기
sum_n = sum(num)
num.sort()
for i in range(8):           # 일곱 난쟁이 찾기
    for j in range(i+1, 9):
        if sum_n-(num[i] + num[j]) == 100:
            num1, num2 = num[i], num[j]
num.remove(num1)
num.remove(num2)

for i in range(7):
    print(num[i])
