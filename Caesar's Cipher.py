# A code that receives a line of text in English as input and encrypts all words.
# Each word of the string is encrypted using the Caesar cipher (cyclic shift by the length of this word).
# Lowercase letters remain lowercase, while uppercase letters remain uppercase.
# Characters that are not English letters do not change.


text = input('Enter the text: ').split()  # создал список из входящей строки
spisok_dlin = list()  # список с длинами слов
new_text = list()  # пустой список, для добавления в него зашифрованых символов
text1 = list()
for i in text:  # цикл на длину слов
    total = 0
    for g in i:
        if g.isalpha() == True:
            total += 1
    spisok_dlin.append(total)

for j in text:  # цикл для добавления к слову символа, который я в конце изменю на пробел
    slovo = j + '+'
    text1.append(slovo)

for g in text1:  # создал крокодила для шифрования букв и добавления символов)))
    for k in range(len(g)):
        if g[k].isalpha() == True:  # проверяю буква это или нет
            if g[k].islower() == True:  # если буква маленькая
                shifr = ord(g[k]) + spisok_dlin[0]
                if shifr < 97:
                    shifr += 26
                if shifr > 122:
                    shifr -= 26
                new_text.append(chr(shifr))  # добавляю полученую зашифрованную букву в пустой список
            if g[k].isupper() == True:  # если буква большая
                shifr = ord(g[k]) + spisok_dlin[0]
                if shifr < 65:
                    shifr += 26
                if shifr > 90:
                    shifr -= 26
                new_text.append(chr(shifr))  # добавляю полученую зашифрованную букву в пустой список
        else:  # если не буква
            shifr = g[k]  # переменной присваиваю значение символа
            new_text.append(shifr)  # добовляю символ в список
    del spisok_dlin[0]  # удаление количества букв первого слова и списка, чтобы следующее слово брало в шаг количество букв следующего слова

stroka = ''.join(new_text)  # создал строку из полученого списка
words = stroka.split('+')
print(*words)