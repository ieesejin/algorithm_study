# https://www.acmicpc.net/problem/1212


# def octalToDecimal(n):
#     res = 0
#     n = str(n)
#     for i in range(len(n)):
#         res += int(n[-(i+1)]) * (8 ** i)
#
#     return int(res)
#
#
# def decimalToBinary(n):
#     res = ''
#     a, b = divmod(n, 2)
#     if a == 0:
#         return str(b) + res
#
#     return decimalToBinary(a) + str(b) + res
#
#
# num = int(input())
#
# print(decimalToBinary(octalToDecimal(num)))

# python library
num = input()
print(bin(int(num, 8)))
