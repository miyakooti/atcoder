n, ans_money = map(int, input().split())

ans = [-1, -1, -1]

for i in range(n+1):
    total_money = i*1000
    if i > n or total_money > ans_money:
        break

    for j in range(n+1):
        total_money = i*1000 + j*5000
        if i+j > n or total_money > ans_money:
            break
        # 枚数は必然的に決まるのでfor文を回す必要はない

        k = n - i - j
        total_money = i*1000 + j*5000 + k*10000

        if total_money == ans_money:
            ans = [k, j, i]


print(f"{ans[0]} {ans[1]} {ans[2]}")

# for i in range(n+1):
#     total_money = i*1000
#     if i > n or total_money > ans_money:
#         break

#     for j in range(n+1):
#         total_money = i*1000 + j*5000
#         if i+j > n or total_money > ans_money:
#             break

#         for k in range(n+1):

#             total_money = i*1000 + j*5000 + k*10000
#             if total_money == ans_money and i+j+k == n:
#                 ans = [k, j, i]
#                 break

# print(f"{ans[0]} {ans[1]} {ans[2]}")


# for i in range(n+1):
#     total_money = i*10000
#     if i > n or total_money > ans_money:
#         break

#     for j in range(n+1):
#         total_money = i*10000 + j*5000
#         if i+j > n or total_money > ans_money:
#             break

#         for k in range(n+1):

#             total_money = i*10000 + j*5000 + k*1000
#             if total_money == ans_money and i+j+k == n:
#                 ans = [i, j, k]
#                 break

# print(f"{ans[0]} {ans[1]} {ans[2]}")


# すべてのforから抜け出すには？
# これ優先的に利用されるのは、1000円ってゆーことだよな
# 最初にループが始まるのは1000円のforだから
