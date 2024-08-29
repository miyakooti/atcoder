# -*- coding: utf-8 -*-

# 入出力
a = int(input())
b, c = map(int, input().split())
l = list(map(int, input().split()))

matlix = [int(input()) for i in range(n)]


# デバッグ用
print("----------")

# uniqueなlist
list(dict.fromkeys(l))


# // 各桁の和を計算する関数
def findSumOfDigits(n: int):
    sum = 0
    while True:

        sum += n % 10
        n /= 10
        n = int(n)

        if n < 1:
            break

    return sum
