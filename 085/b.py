n = int(input())
mochi = [int(input()) for i in range(n)]


mochi = list(set(mochi))
mochi.sort()


count = len(mochi)

print(count)

# # 使わない文字は_
# mochi = [int(input()) for _ in range(n)]

# # uniqueなlistの作成方法
# list(dict.fromkeys(l))
