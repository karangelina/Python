# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Введите месяц в виде целого числа от 1 до 12:"))
if number <= 12 and number >= 1:
    month_dict = {1: "Зима",
                  2: "Зима",
                  3: "Весна",
                  4: "Весна",
                  5: "Весна",
                  6: "Лето",
                  7: "Лето",
                  8: "Лето",
                  9: "Осень",
                  10: "Осень",
                  11: "Осень",
                  12: "Зима"}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Судя по списку на дворе {month_list[i]}")
            break
    print(f"По словарю тоже {month_dict[number]}")
else:
    print("Ошибочка")