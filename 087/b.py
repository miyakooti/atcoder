

n_500 = int(input())
n_100 = int(input())
n_50 = int(input())
x = int(input())


count = 0

for i in range(n_500+1):
    if i*500 > x:
        continue
    for j in range(n_100+1):
        if i*500 + j*100 > x:
            continue
        for k in range(n_50+1):
            sum = i*500 + j*100 + k*50
            if sum == x:
                count += 1


print(count)


# より高度な問題であっても、過度に数学的考察に走ってしまって DP
# といった素直な解法が取れなくなることも競プロあるあるです。
