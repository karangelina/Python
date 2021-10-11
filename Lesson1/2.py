# 2
seconds = int(input("Введите время в секундах:"))
hours = seconds // 3600
minutes = seconds // 60 - hours * 60
seconds = seconds - hours * 3600 - minutes * 60
if hours < 10:
    print('0', hours, end=':', sep='')
else:
    print(hours, end=':')
if minutes < 10:
    print('0', minutes, end=':', sep='')
else:
    print(minutes, end=':')
if seconds < 10:
    print('0', seconds, sep='')
else:
    print(seconds)
