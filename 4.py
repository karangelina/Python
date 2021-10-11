# 4
n = int(input("Введите целое положительное число:"))
b = 0
while n > 0:
    k = n % 10
    n = n // 10
    if b < k:
        b = k
else:
    print(b)
