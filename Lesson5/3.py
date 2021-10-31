#3
"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32"""

data = {"Троцкий": 17678.567, "Соколов": 21567, "Васнецов": 19294, "Лаврентьев": 55667.56, "Иванов": 23543.12, "Петров": 13749.32, "Сидоров": 26585.67, "Васечкин": 23455, "Ульянов": 56777, "Медведев": 12355.67}
try:
    file_obj = open("file_3.txt", "w")
    for last_name, salary in data.items():
        file_obj.write(last_name + ":" + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
sum = 0
count = 0
employees = []
with open("file_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(":")
        if float(tokens[1]) <= 20000:
            employees.append(tokens[0])
        sum += float(tokens[1])
        count += 1
result = sum / count
print(f"persons: {employees}")
print(f"average: {result}")


