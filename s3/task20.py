# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
# которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается
# только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12
str1 = 'A, E, I, O, U, L, N, S, T, R'
value1 = 1
keys = str1.split(", ")
dictionary1 = {}
for i in range(len(keys)):
    dictionary1[keys[i]] = value1
#print(dictionary1)

str2 = 'D, G'
value2 = 2
keys = str2.split(", ")
dictionary2 = {}
for i in range(len(keys)):
    dictionary2[keys[i]] = value2
#print(dictionary2)

str3 = 'B, C, M, P'
value3 = 3
keys = str3.split(", ")
dictionary3 = {}
for i in range(len(keys)):
    dictionary3[keys[i]] = value3
#print(dictionary3)

str4 = 'F, H, V, W, Y'
value4 = 4
keys = str4.split(", ")
dictionary4 = {}
for i in range(len(keys)):
    dictionary4[keys[i]] = value4
#print(dictionary4)

str1_ru = 'А, В, Е, И, Н, О, Р, С, Т'
value1 = 1
keys = str1_ru.split(", ")
dictionary_ru1 = {}
for i in range(len(keys)):
    dictionary_ru1[keys[i]] = value1
#print(dictionary_ru1)

str2_ru = 'Д, К, Л, М, П, У'
value2 = 2
keys = str2_ru.split(", ")
dictionary_ru2 = {}
for i in range(len(keys)):
    dictionary_ru2[keys[i]] = value2
#print(dictionary_ru2)

str3_ru = 'Б, Г, Ё, Ь, Я'
value3 = 3
keys = str3_ru.split(", ")
dictionary_ru3 = {}
for i in range(len(keys)):
    dictionary_ru3[keys[i]] = value3
#print(dictionary_ru3)

str4_ru = 'Й, Ы'
value4 = 4
keys = str4_ru.split(", ")
dictionary_ru4 = {}
for i in range(len(keys)):
    dictionary_ru4[keys[i]] = value4
#print(dictionary_ru4)

str5_ru = 'Ж, З, Х, Ц, Ч'
value5 = 5
keys = str5_ru.split(", ")
dictionary_ru5 = {}
for i in range(len(keys)):
    dictionary_ru5[keys[i]] = value5
#print(dictionary_ru5)

str6_ru = 'Ш, Э, Ю'
value6 = 8
keys = str6_ru.split(", ")
dictionary_ru6 = {}
for i in range(len(keys)):
    dictionary_ru6[keys[i]] = value6
#print(dictionary_ru6)

str7_ru = 'Ф, Щ, Ъ'
value7 = 10
keys = str7_ru.split(", ")
dictionary_ru7 = {}
for i in range(len(keys)):
    dictionary_ru7[keys[i]] = value7
#print(dictionary_ru7)

dict_en = dictionary4 | dictionary3 | dictionary2 |  dictionary1
#print(dict_en)
dict_ru = dictionary_ru7 | dictionary_ru6 | dictionary_ru5 | dictionary_ru4 | dictionary_ru3 | dictionary_ru2 | dictionary_ru1
#print(dict_ru)
dict_all = dict_en | dict_ru

sum = 0
word = str.upper(input('Введиите слово: '))
for key, value in dict_all.items():
    for j in range(len(word)):
        if key == word[j]:
            sum += value

print(f' Ваше количество балов', sum)