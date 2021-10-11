# 6
a = float(input("Введите начальный результат:"))
b = float(input("Введите желаемый результат:"))
k = 1
while a < b:
    a = a * 1.1
    k = k + 1
else:
    print(f"Вам понадбится {k} дней")
