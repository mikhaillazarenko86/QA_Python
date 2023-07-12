# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def arithmetic_progression(first, diff, quantity):
    list = []
    a_n = first
    for i in range(quantity):
        prog = a_n + diff
        a_n = prog
        list.append(a_n)
    print(list)


first = int(input(" введите первый элемент:"))
diff = int(input('Введите шаг прогрессии: '))
quantity = int(input('Введите количество элементов: '))
arithmetic_progression(first, diff, quantity)