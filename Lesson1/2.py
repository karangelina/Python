# 2
seconds = int(input("Введите время в секундах:"))
hours = seconds // 3600
minutes = seconds // 60 - hours * 60
seconds = seconds - hours * 3600 - minutes * 60
if hours < 10:
    hours = int(f"{0}{hours}")
print(hours, minutes, seconds)
