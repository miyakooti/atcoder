# https://atcoder.jp/contests/abc098/submissions/me

# 累積和


N = int(input())
S = (input())

ans = 3*10**5

left_sum = 0
right_sum = 0

# iをリーダーとする
for i in range(N):

    if i == 0:
        left_sum = 0
        right_sum = S[i+1:].count("E")

    else:
        if S[i-1] == "W":
            left_sum += 1
        if S[i] == "E":
            right_sum -= 1

    both = left_sum+right_sum

    ans = min(ans, both)

print(ans)


# N = int(input())
# S = (input())

# ans = 3*10**5

# # iをリーダーとする
# for i in range(N):

#     sum = 0

#     # 左にいる人をEに向かせる = Wのカウント
#     sum += S[:i].count("W")

#     # 右にいる人をWに向かせる
#     sum += S[i+1:].count("E")

#     ans = min(sum, ans)

# print(ans)
