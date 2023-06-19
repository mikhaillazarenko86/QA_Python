# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

#Вариант 1

number = input("Введите трехзначное число: ")
sum = 0
for i in range (0, len(number)):
    sum += int(number[i])
print(sum)

#Вариант 2

input_number = int(input("Введите трехзначное число: "))
first_digit = input_number // 100
second_digit = input_number // 10 % 10
third_digit = input_number % 10
sum = first_digit + second_digit +third_digit
print(sum)
