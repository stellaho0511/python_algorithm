mon = [500, 100, 50, 10, 5, 1]    # 거스름 돈 단위
count = 0
change = 1000 - int(input())   # 거슬러 줄 돈
for i in range(len(mon)):      # 잔돈의 개수  
    count += change // mon[i]
    change = change % mon[i]
print(count)
