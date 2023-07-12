# 4.Создайте список из случайных чисел. Найдите второй максимум.
#
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
import random

# Создание списка из случайных чисел.
def numbers():
    a = int(input("Введите количество элементов: "))
    numbers = []
    for i in range (a):
        n = random.randint(1, 10)
        numbers.append(n)
    return numbers

list_numbers = numbers()
print(list_numbers)
index = list_numbers.index(max(list_numbers))
list_numbers.pop(index)
max_second = max(list_numbers)
print(f"Второе максимальное числло в списке равно {max_second}")