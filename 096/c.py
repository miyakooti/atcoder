# https://atcoder.jp/contests/abc096/tasks/abc096_c

height, width = map(int, input().split())

matlix = [(input()) for _ in range(height)]

# グリッドを見ていって、上下左右にグリッドが含まれているかを見る

ans = "Yes"

hoge = [[]]

for i in range(height):
    for j in range(width):

        if matlix[i][j] == ".":
            continue

        # フラグをなくせる
        go_up = True
        go_down = True
        go_right = True
        go_left = True

        if i == 0:
            go_up = False
        if i == height - 1:
            go_down = False
        if j == 0:
            go_left = False
        if j == width - 1:
            go_right = False

        has_neighbor = False

        if go_up:
            a = matlix[i-1][j]
            if a == "#":
                has_neighbor = True
                continue

        if go_down:
            a = matlix[i+1][j]
            if a == "#":
                has_neighbor = True
                continue

        if go_right:
            a = matlix[i][j+1]
            if a == "#":
                has_neighbor = True
                continue

        if go_left:
            a = matlix[i][j-1]
            if a == "#":
                has_neighbor = True
                continue

        if has_neighbor == False:
            ans = "No"
            break

print(ans)
