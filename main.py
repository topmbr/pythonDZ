#Завдання 1
"""
def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product

numbers = [3, 2, 3, 4]
print(f"Добуток елементів {numbers}: {product_of_elements(numbers)}")
"""
#Завдання 2
"""
def find_minimum(lst):
    if not lst:
        return None
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

numbers = [4, 2, 9, 0.5 , 5]
print(f"Мінімальне значення у списку {numbers}: {find_minimum(numbers)}")
"""
#Завдання 3
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(lst):
    prime_count = 0
    for num in lst:
        if is_prime(num):
            prime_count += 1
    return prime_count

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Кількість простих чисел у списку {numbers}: {count_primes(numbers)}")
"""
#Завдання 4
"""
def remove_number(lst, number):
    initial_length = len(lst)
    lst[:] = [num for num in lst if num != number]
    final_length = len(lst)
    return initial_length - final_length

numbers = [1, 2, 3, 2, 4, 2, 5, 2]
removed_count = remove_number(numbers, 2)
print(f"Кількість видалених елементів: {removed_count}")
print(f"Оновлений список: {numbers}")
"""
#Завдання 5
"""
def merge_lists(lst1, lst2):
    return lst1 + lst2

# Приклад використання
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"Об'єднаний список: {merge_lists(list1, list2)}")
"""
#Завдання 6
"""
def power_elements(lst, power):
    return [num ** power for num in lst]

numbers = [1, 2, 3, 4]
power = 2
print(f"Список {numbers} в ступені {power}: {power_elements(numbers, power)}")
"""