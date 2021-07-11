# 그리디 알고리즘
n = int(input())  # atm 이용할 사람 수
time = list(map(int, input().split())) # 각 사람이 기다리는 시간
time.sort()
sum_t = 0
k = 0
for i in range(len(time)):  # 각 사람이 돈을 인출하는 데 필요한 시간의 최소합
    k += time[i]
    sum_t += k
print(sum_t)
