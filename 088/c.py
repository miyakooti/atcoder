# https://atcoder.jp/contests/abc087/tasks/arc090_a

# どこで下に曲がるかってだけじゃないかな

N = int(input())
height = 2
matlix = [list(map(int, input().split())) for _ in range(height)]


# print(matlix[0][:2])
# print(matlix[0][2:])

ans = 0
for i in range(N):
    candy_sum = 0

    candy_sum += sum(matlix[0][:i+1])

    candy_sum += sum(matlix[1][i:])

    # print(candy_sum)

    ans = max(ans, candy_sum)

print(ans)
