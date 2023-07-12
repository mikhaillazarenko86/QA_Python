# 2.Создайте список из случайных чисел. Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).
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
index = 0
for i in range(1, len(list_numbers) - 1):
    if list_numbers[i] > list_numbers[i + 1] and list_numbers[i] > list_numbers[i - 1]:
        index = i
        num = list_numbers[i]

print(f"Индекс последнего локального максимума (число {num}) = {index}")