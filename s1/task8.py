# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no
chocolate_side_n = int(input("Введите сторону n шоколадки: "))
chocolate_side_m = int(input("Введите сторону m шоколадки: "))
slices_count_k = int(input("Введите количество долек k: "))
chocolate_square = chocolate_side_m *  chocolate_side_n
if slices_count_k > chocolate_side_m or slices_count_k > chocolate_side_n and chocolate_square % slices_count_k == 0 and slices_count_k != 1:
    print(f"Можно отломить от шоколадки {slices_count_k} долек")
else:
    print(f"Нельзя отломить от шоколадки {slices_count_k} долек")