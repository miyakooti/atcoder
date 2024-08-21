# -*- coding: utf-8 -*-


# // 各桁の和を計算する関数


def B():
    n, a, b = map(int, input().split())

    ans = 0
    for i in range(n+1):

        # 0~Nで回していく
        sum_of_digits = findSumOfDigits(i)

        if sum_of_digits >= a and sum_of_digits <= b:
            ans += i

    print(ans)


def A():

    n, a, b = map(int, input().split())

    ans = 0
    for i in range(n+1):

        # "123"
        i_str = str(i)

        sum = 0

        # 合計
        for number in i_str:
            sum += int(number)

        if sum >= a and sum <= b:
            ans += int(i_str)

    print(ans)


def findSumOfDigits(n: int):
    sum = 0
    while True:

        sum += n % 10
        n /= 10
        n = int(n)

        if n < 1:
            break

    return sum


# A()
B()
# print(findSumOfDigits(103))
