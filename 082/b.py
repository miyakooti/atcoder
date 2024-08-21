n = input()
l = map(int, input().split())


count = 0
while True:
    l = [n / 2 for n in l]

    break_flag = False
    for i in l:
        if i != int(i): # 整数でない
            break_flag = True
            break

    if break_flag:
        break
    
    count+=1

print(count)

n = int(input())  # 最初の入力は使っていないので削除
l = list(map(int, input().split()))

count = 0

while all(x % 2 == 0 for x in l):
    l = [x // 2 for x in l]
    count += 1

print(count)



n = int(input())  # 最初の入力は使っていないので削除
l = list(map(int, input().split()))

count = 0

while all(x % 2 == 0 for x in l):
    l = [x // 2 for x in l]
    count += 1

print(count)
