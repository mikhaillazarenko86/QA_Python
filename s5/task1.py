# 1) RLE-сжатие – один из самых простых методов сжатия строки, основанный на сокращении подстрок,
# состоящих из одинаковых символов. Сжатие осуществляется следующим образом:
# Строка разбивается на минимальное количество подстрок, состоящих из одинаковых символов.
# Например, abbcaaa превращается в строки a, bb, c, aaa.
# Каждая из полученных строк превращается в строку, состоящую из числа и буквы.
# Числом является количество повторений символа в этой строке, буква берётся из первого символа обрабатываемой строки. Число не добавляется, если количество символов в строке равно единице. Из предыдущего массива строк мы получаем a, 2b, c, 3a.
# Затем полученные строки конкатенируются в исходном порядке. В рассмотренном примере в итоге получим a2bc3a.
# Вводится строка, нужно сжать ее по алгоритму, описанному выше.


text = input("Введите строку: ")
new_text = ""
prev = ""
count = 0
for char in text:
    if char != prev:
        if prev:
            new_text += str(count) + prev
        count = 1
        prev = char
    else:
        count += 1
else:
    new_text += str(count) + prev


print(new_text)
