#Завдання 1
"""
digit1 = input("Введіть першу цифру: ")
digit2 = input("Введіть другу цифру: ")
digit3 = input("Введіть третю цифру: ")

number = digit1 + digit2 + digit3

print("Сформоване число:", number)
"""
#Завдання 2
"""
number = input("Введіть чотиризначне число: ")

product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])

print("Добуток цифр:", product)
"""
#Завдання 3
"""
meters = float(input("Введіть кількість метрів: "))

centimeters = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
miles = meters * 0.000621371

print("Сантиметри:", centimeters)
print("Дециметри:", decimeters)
print("Міліметри:", millimeters)
print("Милі:", miles)
"""
#Завдання 4
"""
base = float(input("Введіть розмір основи трикутника: "))
height = float(input("Введіть розмір висоти трикутника: "))

area = 0.5 * base * height

print("Площа трикутника:", area)
"""
#Завдання 5
"""
number = input("Введіть чотиризначне число: ")

reversed_number = number[::-1]

print("Перевернуте число:", reversed_number)
"""
#Завдання 1
"""
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

operation = input("Введіть операцію (сума або добуток): ")

if operation == "сума":
    result = num1 + num2 + num3
elif operation == "добуток":
    result = num1 * num2 * num3
else:
    result = "Невідома операція!"

print("Результат:", result)
"""
#Завдання 2
"""
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

operation = input("Введіть операцію (максимум, мінімум або середнє): ")

if operation == "максимум":
    result = max(num1, num2, num3)
elif operation == "мінімум":
    result = min(num1, num2, num3)
elif operation == "середнє":
    result = (num1 + num2 + num3) / 3
else:
    result = "Невідома операція!"

print("Результат:", result)
"""
#Завдання 3
"""
meters = float(input("Введіть кількість метрів: "))

conversion = input("Введіть одиницю вимірювання для конвертації (милі, дюйми, ярди): ")

if conversion == "милі":
    result = meters / 1609.34
elif conversion == "дюйми":
    result = meters * 39.3701
elif conversion == "ярди":
    result = meters * 1.09361
else:
    result = "Невідома одиниця вимірювання!"

print("Результат:", result)
"""
