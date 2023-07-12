# 3. Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
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

count = 1
list_count = []

for i in range(0, len(list_numbers) - 1):
    for j in range(i + 1, len(list_numbers)):
        if list_numbers[i] == list_numbers[j]:
            count += 1
    list_count.append(count)
    count = 1
print(f"Максимальное количество одинаковых элементов {max(list_count)}")