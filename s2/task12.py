# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна
# их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
from random import randint
s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
for i in range(1000):
    n1 = randint(1, s - 1)
    n2 = randint(1, s - n1)
    if n1 + n2 == s and n1 * n2 == p:
        print(n1)
        print(n2)