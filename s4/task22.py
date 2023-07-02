# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел.
list1 = list(map(int, input("Введите первый набор: ").split()))
list2 = list(map(int, input("Введите второй набор: ").split()))
list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            list3.append(list1[i])
numbers = set(list3)
a = sorted(numbers)
print(a)