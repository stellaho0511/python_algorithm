N = int(input())
w = []
for i in range(N):         # 단어 입력
    w.append(input())
w = list(set(w))     # 단어 중복 없애기
w.sort(key = lambda x : (len(x), x))      # 단어 길이가 짧은 것부터/ 길이가 같으면 사전 순으로 정렬
print("\n".join(w))
