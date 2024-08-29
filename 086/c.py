import sys

_ = input()
lines = sys.stdin.read().strip().splitlines()

matrix = [list(map(int, line.split())) for line in lines]

t = 0
x = 0
y = 0


ans = "Yes"
for line in matrix:
    # print("----------")

    t_new = line[0]
    x_new = line[1]
    y_new = line[2]

    t_diff = t_new - t
    x_diff = abs(x - x_new)
    y_diff = abs(y - y_new)

    distance = x_diff + y_diff

    # print(t_diff)
    # print(distance)

    diff = t_diff - distance

    # 時間的に行けないか、その場しのぎができないか
    if diff < 0 or diff % 2 != 0:
        ans = "No"
        break
    else:
        t = t_new
        x = x_new
        y = y_new

print(ans)
